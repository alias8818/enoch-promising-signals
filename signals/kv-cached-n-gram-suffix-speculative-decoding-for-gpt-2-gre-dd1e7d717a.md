# KV-cached n-gram suffix speculative decoding for GPT-2 greedy generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cached-n-gram-suffix-speculative-decoding-for-gpt-2-gre-dd1e7d717a`
Run ID: `kv-cached-n-gram-suffix-speculative-decoding-for-gpt-2-gre-dd1e7d717a-20260529T092232266843+0000`

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

- Parent run decision: N-gram suffix speculative draft for GPT-2 cascade inference: enoch://control-plane/projects/n-gram-suffix-speculative-draft-for-gpt-2-cascade-inference-86b092438eb7/runs/n-gram-suffix-speculative-draft-for-gpt-2-cascade-inference-86b092438eb7-20260529T062001008731+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

The mechanism is locally supported under float32: repeated suffix continuations were accepted at 75.6%, averaging 6.11 accepted tokens per successful draft step, and exact greedy equivalence held. A same-configuration fp16 diagnostic reduced calls but failed exact equivalence, identifying precision policy as a key deployment risk.

## Boundaries and scale limits

Evidence is limited to 1152 generated tokens from fixed prompts on one GB10 GPU using a straightforward PyTorch/Transformers harness. It does not cover larger corpora, batched serving, long-context workloads, optimized kernels, larger models, or production fp16/bf16 exactness.

## Claim scope

On a controlled 12-prompt GPT-2-small greedy decoding test with float32 inference, a KV-cached suffix n-gram speculative verifier exactly matched baseline greedy output while reducing model forward calls by 51.8% and improving harness wall-clock throughput by 1.89x.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is not publication-grade, and fp16 exact-greedy mismatch is a material unresolved limitation.

## Recommended next action

Run a bounded medium confirmation on a larger natural prompt set with float32, bf16, and fp16 modes, and require exact-match or a documented deterministic precision policy before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-corpus precision-safe suffix n-gram speculative decoding for GPT-2
- Success threshold: Exact greedy match on all tested prompts plus at least 30% model forward-call reduction and at least 1.2x wall-clock speedup in the chosen precision policy.
- Stop condition: Stop if exact greedy equivalence fails without a deterministic precision fix, or if forward-call reduction falls below 15% on the medium prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cached-n-gram-suffix-speculative-decoding-for-gpt-2-gre-dd1e7d717a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
