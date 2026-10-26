import { analyzeVolume, loadReviews, read, reviewStatus, volumeFiles } from './content.mjs';

let failures = 0, chains = 0, nodes = 0;
const reviews = loadReviews();
for (const file of volumeFiles()) {
  const path = `volumes/${file}`;
  const stats = analyzeVolume(read(path).toString());
  const status = reviewStatus(path, reviews);
  const problems = [...stats.errors];
  if (process.argv.includes('--require-reviewed') && status.kind !== 'pass') {
    problems.push(`${status.label}: ${(status.stale || []).join(', ')}`);
  }
  console.log(`${file}: ${stats.chains}链/${stats.nodes}节点 · ${status.label}`);
  for (const error of problems) console.error(`  ERROR: ${error}`);
  failures += problems.length;
  chains += stats.chains;
  nodes += stats.nodes;
}
console.log(`合计 ${volumeFiles().length}卷 / ${chains}链 / ${nodes}节点；${failures}项失败`);
process.exitCode = failures ? 1 : 0;
