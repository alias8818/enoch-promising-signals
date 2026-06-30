# Residual-channel int2 KV quantization on real long-context KV traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-int2-kv-quantization-on-real-long-context-15d7510892`
Run ID: `residual-channel-int2-kv-quantization-on-real-long-context-15d7510892-20260621T190420602316+0000`

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

- Parent run decision: Residual-channel int2 quantization for KV cache under long-context CPU eval: enoch://control-plane/projects/residual-channel-int2-quantization-for-kv-cache-under-long-context-cpu-eval-04e1d38a9efb/runs/residual-channel-int2-quantization-for-kv-cache-under-long-context-cpu-eval-04e1d38a9efb-20260621T175135481477+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/408262a02f5a

## What looked useful

Residual-channel protection monotonically improved attention-output relative L2, attention KL, and top-1 attention agreement across three seeds, but the improvement was too small at the 12.5% residual budget and the 25% variant lost the required 4x compression target.

## Boundaries and scale limits

Not tested on downloaded pretrained long-context model KV caches, model perplexity, next-token loss, generation quality, real serving throughput, or hardware memory-bandwidth behavior. Evidence is a controlled mechanism test, not publication-grade validation.

## Claim scope

Controlled Tier 1 CPU test of residual-channel int2 KV quantization on 4096-token causal attention traces generated from byte-tokenized real project/controller text with deterministic transformer-style projections. The 12.5% residual-channel variant improved attention-output error by 11.37% vs all-channel int2 at 4.27x fp16 KV compression, below the 25% success threshold.

## Why it stopped

The bounded direct/proxy test did not meet the stated 25% error-reduction threshold at the required >=4x KV compression, so this is useful no-paper evidence rather than a positive result.

## Recommended next action

Stop this run as an early threshold falsification; if continuing the line, run the same residual-channel int2 test on a small pretrained model's real KV traces with next-token loss deltas.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-model residual-channel int2 KV trace validation
- Success threshold: Residual 12.5% int2 achieves >=25% mean attention-output relative L2 reduction vs all-channel int2, >=4x KV compression vs fp16, and no more than a small bounded next-token loss/perplexity degradation specified before the run.
- Stop condition: Stop if pretrained traces reproduce less than 15% relative L2 improvement at 12.5% residual budget in two independent documents/seeds, or if dependency/runtime requirements exceed the local bounded budget.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-int2-kv-quantization-on-real-long-context-15d7510892`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
