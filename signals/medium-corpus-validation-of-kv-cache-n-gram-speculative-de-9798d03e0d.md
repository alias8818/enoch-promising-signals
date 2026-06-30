# Medium corpus validation of KV-cache n-gram speculative decoding on repeated code and text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-corpus-validation-of-kv-cache-n-gram-speculative-de-9798d03e0d`
Run ID: `medium-corpus-validation-of-kv-cache-n-gram-speculative-de-9798d03e0d-20260522T041204344138+0000`

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

- Parent run decision: Optimized KV-cache n-gram speculative decoding latency test: enoch://control-plane/projects/optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828/runs/optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828-20260522T032104481187+0000
- Parent run decision: N-gram speculative decoding for tiny LLMs with exact draft verification: enoch://control-plane/projects/n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2/runs/n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2-20260521T221318485798+0000

## What looked useful

Across 288 non-greedy float32 rows, exact-match rate was 1.0. The ngram4 draft8 ablation achieved mean acceptance 0.6752, mean target-forward reduction 0.3686, and mean wall-clock speedup 1.5526x. Repeated prompts were stronger than controls for draft8 forward reduction, 0.4000 vs 0.3372, but controls also benefited substantially.

## Boundaries and scale limits

Local GPT-2 only; deterministic local corpus rather than public benchmark corpus; 64-token greedy continuations; Python validation harness with cache deepcopy; low-precision bf16/default run had an exactness failure on one prompt; no large-model, sampling, serving, or production-kernel validation.

## Claim scope

On GPT-2 float32 greedy decoding over 3 fixed seeds and 96 deterministic medium local code/text prompts, KV-cache n-gram speculative decoding exactly matched greedy outputs and reduced target-model forward passes, with strongest results at ngram4 draft8.

## Why it stopped

No-paper closure: medium local evidence supports the mechanism, but the result is not publication-grade because repeated-vs-control separation is modest, controls also benefit, and low-precision exactness failed without stricter handling.

## Recommended next action

Run a bounded deepen validation on real public repeated-code/text benchmarks with low-precision tie-safe exactness checks and optimized KV-cache state handling before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Benchmark-corpus and low-precision validation of exact n-gram speculative decoding
- Success threshold: Exact-match rate 1.0, repeated-prompt draft8 target-forward reduction at least 0.30, repeated prompts at least 0.08 absolute forward-reduction above matched controls, and no low-precision divergence.
- Stop condition: Stop as negative if any exactness divergence remains after tie-safe verification, or if repeated prompts fail to exceed controls by 0.08 absolute forward-reduction on the benchmark corpus.

## Evidence references

- Artifact root: `<local-path>/projects/medium-corpus-validation-of-kv-cache-n-gram-speculative-de-9798d03e0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
