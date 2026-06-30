# Suffix-Tree Draft Speculation with Exact Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-speculation-with-exact-verification-d6418982277e`
Run ID: `suffix-tree-draft-speculation-with-exact-verification-d6418982277e-20260628T135329788812+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/9f1b043331c8

## What looked useful

Exact verification is feasible: all GPT-2 speculative outputs matched greedy outputs. Multi-token suffix drafts reduced forward calls from 512 to 244 overall; repeated prose/code reduced calls from 256 to 75, while natural prompts reduced calls from 256 to 169. A max_draft=1 ablation kept calls at 512, showing the useful mechanism is multi-token exact verification rather than suffix matching alone.

## Boundaries and scale limits

Small prompt set, greedy decoding only, GPT-2 small only, KV-cache optimized implementation not tested, no large corpus, no sampling, no latency benchmark under production batching.

## Claim scope

On eight local GPT-2-small prompts, suffix-index draft speculation with exact greedy verification preserved exact greedy outputs and reduced target-model forward calls on repetition-heavy prompts, with smaller but positive call reduction on the included natural prompts.

## Why it stopped

Bounded local evidence supports the mechanism but is not publication-grade; the result is a small GPT-2 greedy-decoding study, not a broad validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a KV-cache exact verifier and evaluate on a larger pre-registered corpus with latency and acceptance-rate controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix speculation on a larger repetition-stratified corpus
- Success threshold: All outputs exactly match greedy; repetition-heavy stratum achieves at least 1.25x median wall-clock speedup and at least 2x median target-call reduction; natural stratum median latency is no worse than 1.05x greedy.
- Stop condition: Stop if exactness fails on any prompt after debugging, or if repetition-heavy median wall-clock speedup is below 1.10x with a KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-speculation-with-exact-verification-d6418982277e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
