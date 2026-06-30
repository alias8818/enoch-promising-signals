# CPU-Bound Speculative Decoding: N-gram Baseline vs No-Speculation on Local Hardware

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bound-speculative-decoding-n-gram-baseline-vs-no-speculation-on-local-hardware-8caa9bc391d0`
Run ID: `cpu-bound-speculative-decoding-n-gram-baseline-vs-no-speculation-on-local-hardware-8caa9bc391d0-20260614T092758593508+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

N-gram speculation was exact and sometimes faster, but the primary distilgpt2 run reached only 1.0351x mean speedup with 3.125% mean target-forward reduction; plain text was neutral at 1.0001x with no target-forward reduction.

## Boundaries and scale limits

Only distilgpt2 and sshleifer/tiny-gpt2 were tested; the verifier used full-prefix forwards rather than KV-cache-aware verification; prompt set had three prompts; primary run generated 64 tokens per prompt; no batched serving, concurrency, larger LLMs, or production CPU inference engine was tested.

## Claim scope

On a local CPU worker using distilgpt2, a simple full-prefix n-gram prompt-lookup speculative decoder preserved exact greedy output and produced small throughput gains on repetitive/code-like prompts, but did not sustain meaningful speedup across the bounded 64-token prompt set.

## Why it stopped

Bounded local evidence was mixed: exactness held, but primary speedup was too small and prompt-dependent for a paper-ready or broad CPU-serving claim.

## Recommended next action

Stop this run as no-paper useful signal; if deepening, implement KV-cache-aware n-gram verification and require sustained multi-token draft acceptance before testing larger prompt sets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware n-gram speculative decoding on CPU repeated-code workloads
- Success threshold: Mean speedup >= 1.15x, min prompt speedup >= 1.00x, exact greedy equality for every prompt, and mean target-forward reduction >= 20% on the bounded CPU benchmark.
- Stop condition: Stop as negative if exact equality fails or if mean speedup remains below 1.10x after KV-cache-aware verification on the bounded repeated-code/prose prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bound-speculative-decoding-n-gram-baseline-vs-no-speculation-on-local-hardware-8caa9bc391d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
