import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { loadReviews, reviewStatus, root, volumeFiles } from './content.mjs';

const site = join(root, 'site');
const manifest = JSON.parse(readFileSync(join(site, 'manifest.json')));
const index = readFileSync(join(site, 'index.html'), 'utf8');
assert.equal(manifest.volumes.length, 7, '预期七卷');
assert.equal(manifest.totals.chains, 98);
assert.equal(manifest.totals.nodes, 394);
assert.deepEqual(manifest.volumes.map(v => v.file), volumeFiles().map(f => f.replace(/\.md$/, '.html')));
const reviews = loadReviews();
for (const volume of manifest.volumes) {
  const current = reviewStatus(`volumes/${volume.file.replace(/\.html$/, '.md')}`, reviews);
  assert.deepEqual(volume.status, current, '渲染状态已过期');
  // 维护者决策（2026-10-27，WORKFLOW.md）：免复检直接发布；快照状态只要求如实渲染，不再要求 PASS。
  assert.ok(index.includes(`href="./${volume.file}"`));
  const html = readFileSync(join(site, volume.file), 'utf8');
  assert.equal((html.match(/<details class="chain"/g) || []).length, volume.chains);
  assert.equal((html.match(/<\/details>/g) || []).length, volume.chains);
  assert.ok(html.includes('name="viewport"'));
  assert.ok(html.includes(volume.status.label));
  for (let i = 1; i <= volume.chains; i++) assert.ok(html.includes(`id="c${String(i).padStart(2, '0')}"`));
  for (const [, path] of html.matchAll(/href="\.\/([^"#]+)"/g)) {
    assert.ok(existsSync(join(site, path)), `${volume.file} 链接不存在: ${path}`);
  }
}
console.log(`站点检查通过：7卷、${manifest.totals.chains}链、${manifest.totals.nodes}节点；折叠、锚点、相邻卷链接与状态一致。`);
