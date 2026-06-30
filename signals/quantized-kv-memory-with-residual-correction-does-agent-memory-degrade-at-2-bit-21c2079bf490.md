# Quantized KV memory with residual correction: does agent memory degrade at 2-bit?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-memory-with-residual-correction-does-agent-memory-degrade-at-2-bit-21c2079bf490`
Run ID: `quantized-kv-memory-with-residual-correction-does-agent-memory-degrade-at-2-bit-21c2079bf490-20260611T205658499579+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/083e54a74394

## What looked useful

At n_mem=1024 and query_noise=2.0, 2-bit no-residual target accuracy was 0.484 versus 0.618 full precision, with argmax agreement 0.624, output cosine 0.748, and attention KL 0.407; 3-bit and 4-bit were much closer at 0.583 and 0.609. At n_mem=4096 and query_noise=2.0, 2-bit accuracy was 0.353 versus 0.475 full precision; a 256-token recent residual cache covered only 6.2% of targets and left accuracy at 0.350, while high-error 256-token correction reached only 0.370.

## Boundaries and scale limits

No real transformer activations, no autoregressive generation, no agent task traces, no production KV quantization kernels, and no GPT-2-small-class or larger benchmark. The evidence is mechanism-level and proxy-only, not a full validation of deployed agent memory.

## Claim scope

Synthetic attention-retrieval probe with random Gaussian K/V memories, per-token affine KV quantization, memory lengths 256/1024/4096, d_head=64, 512 trials per seed, and 3 seeds. Within this proxy, 2-bit KV quantization degrades target retrieval and attention/output fidelity at moderate and hard retrieval margins; small recent residual caches do not repair old-memory degradation except in proportion to target coverage.

## Why it stopped

Proxy evidence supports 2-bit degradation and limited residual-cache repair, but scientific closure for agent memory requires direct transformer/task evidence.

## Recommended next action

Stop this proxy run as no-paper useful signal; run a bounded direct follow-up on a small transformer with real incremental KV-cache quantization and needle-in-context or associative-recall prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer KV-cache quantization on real retrieval prompts
- Success threshold: 2-bit shows at least a 10 percentage point old-needle accuracy drop versus full precision or 4-bit, while recent residual correction recovers recent-needle accuracy without recovering old-needle accuracy.
- Stop condition: Stop if a smoke test cannot reproduce correct full-precision retrieval above 80% on the chosen prompts, or if 2-bit, 3-bit, and 4-bit are indistinguishable across old and recent needles in a calibrated medium run.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-memory-with-residual-correction-does-agent-memory-degrade-at-2-bit-21c2079bf490`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
