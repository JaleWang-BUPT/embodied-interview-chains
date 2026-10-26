import test from 'node:test';
import assert from 'node:assert/strict';
import { analyzeVolume, answerLength, reviewStatus, sha256 } from '../tools/content.mjs';

test('review PASS binds every snapshot input, not just volume text', () => {
  const files = { 'volumes/test.md': 'answer', 'research/source.md': 'source' };
  const reviews = [{ file: 'review.json', data: {
    target: 'volumes/test.md', round: 2, verdict: 'PASS', independent_context: true, model: 'review-test',
    snapshot_sha256: Object.fromEntries(Object.entries(files).map(([p, text]) => [p, sha256(text)])),
  } }];
  const read = path => files[path];
  assert.equal(reviewStatus('volumes/test.md', reviews, read).kind, 'pass');
  files['research/source.md'] = 'edited';
  assert.equal(reviewStatus('volumes/test.md', reviews, read).kind, 'stale');
});

test('a newer FAIL cannot be hidden by an older matching PASS', () => {
  const reviews = [
    { file: 'old', data: { target: 'volumes/test.md', round: 1, verdict: 'PASS' } },
    { file: 'new', data: { target: 'volumes/test.md', round: 2, verdict: 'FAIL' } },
  ];
  const result = reviewStatus('volumes/test.md', reviews);
  assert.equal(result.kind, 'pending');
  assert.equal(result.record, 'new');
  assert.equal(reviewStatus('absent.md', reviews).kind, 'pending');
  assert.equal(reviewStatus('volumes/test.md', reviews.slice(0, 1)).kind, 'legacy');
});

test('conflicting rounds or missing independent model metadata cannot pass', () => {
  const data = { target: 'volumes/test.md', round: 1, verdict: 'PASS',
    independent_context: true, reviewer_model: 'review-test',
    snapshot_sha256: { 'volumes/test.md': sha256('text') } };
  const read = () => 'text';
  const record = data => ({ file: 'test.json', data });
  assert.equal(reviewStatus('volumes/test.md', [record(data)], read).kind, 'pass');
  assert.equal(reviewStatus('volumes/test.md', [record(data), record({ ...data, verdict: 'FAIL' })], read).kind, 'pending');
  for (const altered of [{ ...data, independent_context: false }, { ...data, reviewer_model: '' },
                        { ...data, snapshot_sha256: { 'volumes/test.md': 'invalid' } }]) {
    assert.equal(reviewStatus('volumes/test.md', [record(altered)], read).kind, 'pending');
  }
});

test('answer length ignores formatting and whitespace, not LaTeX commands', () => {
  assert.equal(answerLength(' **ab** `$x$` 中 '), 4);
  assert.equal(answerLength('$\\frac{a}{b}$'), 11);
});

const sample = `本卷 **1 条链 · 2 个问答节点**
难度分布：L1 **0** · L2 **1** · L3 **0**
<details class="chain">
<summary><span class="lv lv-l2">L2</span><span class="freq">〔推断〕</span><b>C01</b></summary>
**答**：主答。
**追问 1**：为什么？
**答**：追答。
**易错**：工程归纳。
**实录**：推断。
</details>`;

test('validator detects unbalanced tags, wrong counts, IDs and long answers', () => {
  assert.deepEqual(analyzeVolume(sample).errors, []);
  for (const changed of [
    sample.replace('</details>', ''), sample.replace('2 个', '3 个'),
    sample.replace('C01', 'C03'), sample.replace('追答。', '长'.repeat(151)),
    sample.replace('追问 1', '追问 2'), sample.replace('**易错**', '**其他**'),
  ]) assert.ok(analyzeVolume(changed).errors.length);
});
