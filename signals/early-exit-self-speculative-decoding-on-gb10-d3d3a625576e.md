# Early-exit self-speculative decoding on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculative-decoding-on-gb10-d3d3a625576e`
Run ID: `early-exit-self-speculative-decoding-on-gb10-d3d3a625576e-20260621T173523171196+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8c1f51c1f150

## What looked useful

All intermediate exits failed the mechanism threshold. Layers 1-10 had 6.96%-35.82% final-layer greedy agreement; layer 11 reached 53.87% but costs 91.67% of the model. The best estimated setting, layer 1 with gamma 2, was 0.9874x relative speed and accepted only 0.152 drafted tokens per iteration on average.

## Boundaries and scale limits

Bounded proxy test only: GPT-2, 388 prompt positions, greedy agreement, synthetic/local prompts, and estimated speculative speedup rather than a real KV-cache speculative decoder. Does not rule out trained auxiliary heads, confidence gates, token-set acceptance, larger models, or models trained for intermediate-layer draftability.

## Claim scope

On GB10 with pretrained GPT-2 and a small local prompt suite, reusing intermediate hidden states plus the final LM head as a same-model drafter did not produce enough greedy agreement to justify implementing a longer KV-cache self-speculative decoder.

## Why it stopped

Proxy early falsification: direct hidden-state agreement and conservative speed estimates did not clear the minimum mechanism threshold; full validation would require a real KV-cache speculative decoder and broader workloads.

## Recommended next action

Stop this no-paper path unless a bounded follow-up trains or calibrates explicit early-exit draft heads and demonstrates at least 70% agreement with direct tokens/s gains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit draft heads for GPT-2 self-speculation
- Success threshold: At least one exit at <=50% model depth reaches >=70% final-layer greedy agreement and a real speculative decoder shows >=1.10x tokens/s over a KV-cache greedy baseline on held-out prompts.
- Stop condition: Stop if trained/calibrated exits remain below 70% agreement or if direct decoder throughput is <=1.0x baseline after verifier fallback overhead.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-on-gb10-d3d3a625576e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
