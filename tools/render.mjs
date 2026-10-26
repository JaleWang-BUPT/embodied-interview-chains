// 追问链题库渲染器：volumes/*.md → site/*.html + site/index.html
// 零依赖，Node >= 18。渲染目标是我们自定义的受限 Markdown 子集。
import { readFileSync, writeFileSync, mkdirSync, readdirSync, unlinkSync } from 'node:fs';
import { join, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
import { analyzeVolume, loadReviews, reviewStatus, volumeFiles } from './content.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const volDir = join(root, 'volumes');
const siteDir = join(root, 'site');
mkdirSync(siteDir, { recursive: true });
// This directory contains only generated output. Remove stale generated pages,
// never recurse into the workspace or erase unrelated assets.
for (const file of readdirSync(siteDir)) {
  if (file === 'index.html' || file === 'manifest.json' || /^vol\d.*\.html$/.test(file)) {
    unlinkSync(join(siteDir, file));
  }
}

const REPO = 'https://github.com/JaleWang-BUPT/embodied-interview-chains';
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function inline(s) {
  const math = [];
  s = s.replace(/\$\$[^$]+\$\$|\$[^$\n]+\$/g, m => { math.push(m); return `\u0000M${math.length - 1}\u0000`; });
  s = esc(s);
  s = s.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
  s = s.replace(/\u0000M(\d+)\u0000/g, (_, i) => math[i]);
  return s;
}

function renderBody(md) {
  const out = [];
  let para = [], list = null, note = [];
  const flushPara = () => { if (para.length) { out.push('<p>' + para.map(inline).join('<br>') + '</p>'); para = []; } };
  const flushList = () => { if (list) { out.push(`<${list.t}>` + list.items.join('') + `</${list.t}>`); list = null; } };
  const flushNote = () => { if (note.length) { out.push('<div class="note">' + note.map(inline).join('<br>') + '</div>'); note = []; } };

  for (const raw of md.split(/\r?\n/)) {
    const line = raw.trimEnd();
    if (/^<details\b/.test(line)) { flushPara(); flushList(); flushNote(); out.push(line); continue; }
    if (/^<\/details>/.test(line)) { flushPara(); flushList(); out.push(line); continue; }
    if (inRaw(line)) { flushPara(); flushList(); out.push(line); continue; }
    if (/^# /.test(line)) { flushPara(); flushList(); flushNote(); out.push('<h1>' + inline(line.slice(2)) + '</h1>'); continue; }
    if (/^## /.test(line)) { flushPara(); flushList(); flushNote(); out.push('<h2>' + inline(line.slice(3)) + '</h2>'); continue; }
    if (/^> /.test(line)) { flushPara(); flushList(); note.push(line.slice(2)); continue; }
    if (/^---+$/.test(line)) { flushPara(); flushList(); flushNote(); out.push('<hr>'); continue; }
    if (/^- /.test(line)) { flushPara(); flushNote(); if (!list || list.t !== 'ul') { flushList(); list = { t: 'ul', items: [] }; } list.items.push('<li>' + inline(line.slice(2)) + '</li>'); continue; }
    if (/^\d+\. /.test(line)) { flushPara(); flushNote(); if (!list || list.t !== 'ol') { flushList(); list = { t: 'ol', items: [] }; } list.items.push('<li>' + inline(line.replace(/^\d+\. /, '')) + '</li>'); continue; }
    if (/^$/.test(line)) { flushPara(); flushList(); flushNote(); continue; }
    flushNote(); para.push(line);
  }
  flushPara(); flushList(); flushNote();
  return out.join('\n');
  function inRaw(l) { return /^<\/?summary>/.test(l) || /^<summary>/.test(l); }
}

const CSS = `
:root{--bg:#faf9f5;--bg-soft:#f0eee6;--card:#ffffff;--fg:#1f1e1d;--mut:#6e6b64;--faint:#87847e;--line:#e5e1d8;--line-strong:#d9d3c5;--acc:#c96442;--acc-strong:#b04f31;--ok:#71855c;--warn:#a1732c;--bad:#b15b4c}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.85 Georgia,"Noto Serif SC","Source Han Serif SC","Songti SC","SimSun",serif}
::selection{background:#f2d8cc}
main{max-width:800px;margin:0 auto;padding:36px 20px 90px}
h1,h2,.top .brand{font-family:Georgia,"Noto Serif SC","Source Han Serif SC","Songti SC","SimSun",serif;font-weight:600}
h1{font-size:30px;line-height:1.35;margin:.3em 0 .3em}
h2{font-size:21px;margin:2.4em 0 .7em;padding-bottom:.35em;border-bottom:1px solid var(--line)}
p{margin:.8em 0}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline;color:var(--acc-strong)}
code{background:var(--bg-soft);border:1px solid var(--line);border-radius:5px;padding:.05em .4em;font-size:.9em;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
hr{border:none;border-top:1px solid var(--line);margin:2.4em 0}
.note{background:var(--bg-soft);border-left:3px solid var(--acc);border-radius:0 10px 10px 0;padding:12px 18px;margin:16px 0;font-size:15.5px;color:#4a463c;line-height:1.75}
details.chain{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:8px 22px;margin:16px 0;box-shadow:0 1px 2px rgba(60,50,30,.04);transition:border-color .15s}
details.chain:hover{border-color:var(--line-strong)}
details.chain[open]{border-color:var(--line-strong);background:#fffdf9}
summary{cursor:pointer;font-weight:600;font-size:17.5px;padding:10px 0;list-style:none;position:relative;padding-right:76px;overflow-wrap:anywhere}
summary::-webkit-details-marker{display:none}
summary::after{content:'展开';position:absolute;right:0;top:10px;font-size:12.5px;color:var(--mut);background:var(--bg-soft);border-radius:20px;padding:2px 12px;font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif}
details.chain[open] summary::after{content:'收起'}
details.chain[open]>summary{border-bottom:1px solid var(--line);margin-bottom:8px}
.lv{display:inline-block;font-size:11.5px;font-weight:700;border-radius:6px;padding:1px 8px;margin-right:6px;vertical-align:2px;color:#fff;font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif}
.lv-l1{background:var(--ok)}.lv-l2{background:var(--acc)}.lv-l3{background:var(--bad)}
.freq{color:var(--warn);font-size:14.5px;margin-right:8px}
.top{border-bottom:1px solid var(--line);background:var(--bg-soft)}
.top nav{max-width:800px;margin:0 auto;padding:16px 20px;display:flex;gap:20px;align-items:baseline;flex-wrap:wrap}
.top .brand{font-weight:700;color:var(--fg);font-size:16.5px}
.top .brand::before{content:'✳ ';color:var(--acc)}
.top a{font-size:14.5px;font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif}
footer{border-top:1px solid var(--line);margin-top:70px;background:var(--bg-soft)}
footer div{max-width:800px;margin:0 auto;padding:20px;color:var(--faint);font-size:13.5px;line-height:1.7}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px;margin:16px 0;box-shadow:0 1px 2px rgba(60,50,30,.04)}
.card h2{border:none;margin:0 0 6px;font-size:19px}
.card h2 a{color:var(--fg)}.card h2 a:hover{color:var(--acc)}
.meta{color:var(--faint);font-size:14px}
.review{font-size:14px;border-left:3px solid var(--ok);background:#f2f4ea;padding:10px 14px;margin:16px 0;border-radius:0 10px 10px 0;overflow-wrap:anywhere}
.review.pending,.review.stale,.review.legacy{border-color:var(--warn);background:#f7f1e0}
.volume-nav{display:flex;flex-wrap:wrap;gap:12px;margin:20px 0;font-size:14px}
p,li,.note{overflow-wrap:anywhere}
@media(max-width:640px){main{padding:22px 14px 60px}h1{font-size:25px}summary{font-size:16px;padding-right:72px}summary::after{top:6px}}
`;

function page(title, body, rel) {
  return `<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']],displayMath:[['$$','$$']]},chtml:{displayAlign:'left'}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>${CSS}</style>
</head>
<body>
<div class="top"><nav><span class="brand">具身智能面试追问链</span><a href="${rel}">卷目录</a><a href="${REPO}" target="_blank" rel="noopener">GitHub</a></nav></div>
<main>
${body}
</main>
<footer><div>公开面经、整理与推断练习分档标注 · 题源限制与审查范围见各链和记录 · 公式排版使用 MathJax，折叠无需 JavaScript · <a href="${REPO}/blob/main/LICENSE" target="_blank" rel="noopener">MIT License</a> · 渲染于 ${new Date().toISOString().slice(0, 10)}</div></footer>
</body>
</html>`;
}

const files = volumeFiles();
const vols = [];
const reviews = loadReviews();
const reviewBadge = status => `<div class="review ${status.kind}">${esc(status.label)}${status.record ? ` · <a href="${REPO}/blob/main/${status.record}" target="_blank" rel="noopener">审查记录与范围</a>` : ''}</div>`;
for (const [i, f] of files.entries()) {
  const md = readFileSync(join(volDir, f), 'utf8');
  const titleLine = (md.match(/^# (.+)$/m) || ['', basename(f, '.md')])[1];
  const { chains, nodes, errors } = analyzeVolume(md);
  if (errors.length) throw new Error(`${f}: ${errors.join('; ')}`);
  const status = reviewStatus(`volumes/${f}`, reviews);
  const links = `<nav class="volume-nav">${i ? `<a href="./${files[i-1].replace(/\.md$/, '.html')}">← 上一卷</a>` : ''}<a href="./index.html">全部七卷</a>${i+1<files.length ? `<a href="./${files[i+1].replace(/\.md$/, '.html')}">下一卷 →</a>` : ''}<a href="${REPO}/blob/main/volumes/${f}" target="_blank" rel="noopener">Markdown 源文</a></nav>`;
  let chainNumber = 0;
  const body = renderBody(md.replace(/^> 审查状态：.*\n/m, '')).replace(/<details class="chain">/g,
    () => `<details class="chain" id="c${String(++chainNumber).padStart(2, '0')}">`);
  const html = page(titleLine, reviewBadge(status) + links + body + links, './index.html');
  const outName = f.replace(/\.md$/, '.html');
  writeFileSync(join(siteDir, outName), html);
  vols.push({ file: outName, title: titleLine, chains, nodes, status });
  console.log(`rendered ${outName}: ${chains} 链 / ${nodes} 节点`);
}

const cards = vols.map(v => `<div class="card"><h2><a href="./${v.file}">${inline(v.title)}</a></h2><div class="meta">${v.chains} 条追问链 · ${v.nodes} 个问答节点</div>${reviewBadge(v.status)}</div>`).join('\n');
const totals = vols.reduce((sum, v) => ({ chains: sum.chains + v.chains, nodes: sum.nodes + v.nodes }), { chains: 0, nodes: 0 });
const idxBody = `
<h1>具身智能面试追问链</h1>
<p class="meta">${vols.length} 卷 · ${totals.chains} 条追问链 · ${totals.nodes} 个问答节点</p>
<div class="note">主问 → 追问 → 深挖。先自己答，再展开对照，合上后复述整条链。<br>区分公开实录、整理、索引/历史存证和推断练习；公司归属与频次不超出证据。链内细化或重排另行注明。<br>审查状态按最新记录及文件 SHA-256 计算，修改内容后不会沿用旧 PASS；PASS 不代表面试经历真实性认证。</div>
${cards}`;
writeFileSync(join(siteDir, 'index.html'), page('具身智能面试追问链 · 卷目录', idxBody, './index.html'));
writeFileSync(join(siteDir, 'manifest.json'), JSON.stringify({ volumes: vols, totals }, null, 2) + '\n');
console.log('rendered index.html');
