// Shared content checks and snapshot-bound review state. No third-party packages.
import { createHash } from 'node:crypto';
import { readFileSync, readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const root = join(dirname(fileURLToPath(import.meta.url)), '..');
export const read = path => readFileSync(join(root, path));
export const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');
export const volumeFiles = () => {
  const files = readdirSync(join(root, 'volumes')).filter(f => f.endsWith('.md')).sort();
  const unexpected = files.filter(f => !/^vol\d.*\.md$/.test(f));
  if (unexpected.length) throw new Error(`未纳入命名规则的卷文件: ${unexpected.join(', ')}`);
  return files;
};
export const answerLength = text => [...text.replace(/\*\*|`|\$|\s/g, '')].length;

export function analyzeVolume(md) {
  const errors = [];
  const blocks = [...md.matchAll(/<details class="chain">([\s\S]*?)<\/details>/g)];
  const difficulty = { L1: 0, L2: 0, L3: 0 };
  let nodes = 0;
  if (!blocks.length) errors.push('没有追问链');
  if ((md.match(/<details\b/g) || []).length !== blocks.length ||
      (md.match(/<\/details>/g) || []).length !== blocks.length) errors.push('details 标签未配对');
  blocks.forEach(([_, body], index) => {
    const id = `C${String(index + 1).padStart(2, '0')}`;
    if (!body.includes(`<b>${id}</b>`)) errors.push(`${id}: 编号不连续`);
    const summary = body.match(/^<summary>(.+)<\/summary>$/m)?.[1] || '';
    const level = summary.match(/class="lv lv-l([123])"/);
    if (!level) errors.push(`${id}: 缺少难度`);
    else difficulty[`L${level[1]}`]++;
    if (!/class="freq"/.test(summary)) errors.push(`${id}: 缺少来源分档`);
    const follows = [...body.matchAll(/^\*\*追问 (\d+)\*\*/gm)];
    follows.forEach((match, i) => {
      if (+match[1] !== i + 1) errors.push(`${id}: 追问编号不连续`);
    });
    const answers = [...body.matchAll(/^\*\*答\*\*[^：\n]*：(.+)$/gm)];
    if (answers.length !== follows.length + 1) errors.push(`${id}: 问答数量不一致`);
    answers.forEach((answer, i) => {
      const size = answerLength(answer[1]);
      if (size > (i ? 150 : 350)) errors.push(`${id} 答${i}: ${size}字超限`);
    });
    if (!/^\*\*易错\*\*：.+/m.test(body)) errors.push(`${id}: 缺少易错`);
    if (!/^\*\*实录\*\*：.+/m.test(body)) errors.push(`${id}: 缺少题源说明`);
    nodes += follows.length + 1;
  });
  const declared = md.match(/本卷 \*\*(\d+) 条链 · (\d+) 个问答节点/);
  if (!declared || +declared[1] !== blocks.length || +declared[2] !== nodes) errors.push('卷首链数/节点数与正文不符');
  const levels = md.match(/难度分布：L1 \*\*(\d+)\*\* · L2 \*\*(\d+)\*\* · L3 \*\*(\d+)\*\*/);
  if (!levels || ['L1', 'L2', 'L3'].some((level, i) => difficulty[level] !== +levels[i + 1])) errors.push('卷首难度统计与正文不符');
  return { chains: blocks.length, nodes, difficulty, errors };
}

export function loadReviews() {
  return readdirSync(join(root, 'research/reviews')).filter(f => f.endsWith('.json')).map(file => ({
    file: `research/reviews/${file}`,
    data: JSON.parse(read(`research/reviews/${file}`).toString()),
  }));
}

export function reviewStatus(volume, reviews, readFile = read) {
  const candidates = reviews.filter(({ data }) =>
    data.snapshot_sha256?.[volume] || String(data.target || '').includes(volume)
  ).sort((a, b) => (b.data.round || 0) - (a.data.round || 0));
  const latest = candidates[0];
  if (!latest) return { kind: 'pending', label: '待独立审查' };
  const rounds = candidates.map(({ data }) => data.round);
  if (rounds.some(round => !Number.isInteger(round) || round < 1) ||
      new Set(rounds).size !== rounds.length) return {
    kind: 'pending', label: '审查轮号冲突或无效 · 待核验', record: latest.file,
  };
  if (latest.data.verdict !== 'PASS') return {
    kind: 'pending', label: `审查 ${latest.data.verdict} · 待复检`, record: latest.file,
  };
  const snapshot = latest.data.snapshot_sha256;
  if (!snapshot?.[volume]) return {
    kind: 'legacy', label: '历史审查通过 · 无快照校验', record: latest.file,
  };
  const model = latest.data.reviewer_model || latest.data.model;
  if (latest.data.independent_context !== true || typeof model !== 'string' || !model.trim()) return {
    kind: 'pending', label: '独立审查元数据缺失 · 待核验', record: latest.file,
  };
  if (Object.values(snapshot).some(value => typeof value !== 'string' || !/^[a-f0-9]{64}$/.test(value))) return {
    kind: 'pending', label: '审查快照格式错误 · 待核验', record: latest.file,
  };
  const stale = Object.entries(snapshot).filter(([path, expected]) => {
    try { return sha256(readFile(path)) !== expected; }
    catch { return true; }
  }).map(([path]) => path);
  if (stale.length) return { kind: 'stale', label: '内容已变更 · 待复检', record: latest.file, stale };
  return { kind: 'pass', label: `独立审查 PASS · 第${latest.data.round}轮 · 快照匹配`, record: latest.file };
}
