# Medium Confirmation of Context N-Gram Speculative Decoding with Optimized KV Rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-confirmation-of-context-n-gram-speculative-decoding-8394496bef`
Run ID: `medium-confirmation-of-context-n-gram-speculative-decoding-8394496bef-20260529T040913605795+0000`

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

- Parent run decision: Live KV-Cache Context N-Gram Speculative Decoder on Natural Long-Context Corpora: enoch://control-plane/projects/live-kv-cache-context-n-gram-speculative-decoder-on-natura-fc82282c87/runs/live-kv-cache-context-n-gram-speculative-decoder-on-natura-fc82282c87-20260529T020611061234+0000
- Parent run decision: Context-Local N-Gram Speculative Drafting with Zero Extra VRAM: enoch://control-plane/projects/context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d/runs/context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d-20260528T232933276261+0000

## What looked useful

The n-gram proposer mechanism is supported for repeated-context prompts: high acceptance and batched verification drive exact decoding speedups. Optimized rollback is only weakly supported; it helps about 10%-11% in rejection-heavy random controls but is effectively tied with naive rollback for the actual high-acceptance n-gram proposer.

## Boundaries and scale limits

Small cached GPT-2-class model, synthetic/repetition-rich prompt set, greedy single-sequence decoding only, no long natural corpus, no larger instruction model, no batch serving, no sampling, and no production kernel integration.

## Claim scope

On 16 repetition-rich prompts, 3 fixed seeds, distilgpt2 greedy decoding, and 64 generated tokens per prompt, context n-gram speculative decoding exactly matched greedy outputs and improved throughput by 1.4x to 3.5x versus a greedy KV baseline while reducing target forward calls to 0.35x to 0.63x of baseline.

## Why it stopped

Medium local evidence supports the n-gram acceptance mechanism but not a paper-ready optimized-rollback claim; this should close as no-paper useful signal.

## Recommended next action

Run a bounded deepen test on natural prompt corpora and one larger local model, requiring n-gram optimized decoding to beat greedy by at least 1.2x with exact outputs and to beat naive rollback only when rejection rate is nontrivial.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus and larger-model check for context n-gram speculative decoding
- Success threshold: Across natural prompt sets, n-gram optimized decoding must exactly match greedy outputs, achieve geometric mean speedup >= 1.2x over greedy KV, keep random control below greedy, and show optimized rollback exceeds naive rollback by >= 5% only in bins with at least 10 rejected drafts per prompt.
- Stop condition: Stop if exactness fails, if n-gram optimized speedup is < 1.05x on both natural prompt sets, or if acceptance falls below 0.5 without a compensating target-forward reduction.

## Evidence references

- Artifact root: `<local-path>/projects/medium-confirmation-of-context-n-gram-speculative-decoding-8394496bef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
