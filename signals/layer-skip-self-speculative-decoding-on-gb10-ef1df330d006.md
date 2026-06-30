# Layer-Skip Self-Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-skip-self-speculative-decoding-on-gb10-ef1df330d006`
Run ID: `layer-skip-self-speculative-decoding-on-gb10-ef1df330d006-20260621T011606102336+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ead18c512662

## What looked useful

Exit-layer agreement rose with depth but remained insufficient for speedup: layer 4 top-1 15.43% estimated 0.56x, layer 6 top-1 21.09% estimated 0.53x, layer 8 top-1 30.08% estimated 0.53x, and layer 10 top-1 50.78% estimated 0.67x. High-confidence layer-10 tokens matched 81.59%, suggesting confidence gating may be worth testing only on trained early-exit models.

## Boundaries and scale limits

Tested one 12-layer GPT-2-small-class checkpoint, 16 fixed prompts, 512 generated positions, greedy decoding, fp16 CUDA inference, and timing proxies rather than an optimized self-speculative serving implementation. Does not evaluate LayerSkip-trained checkpoints, larger Llama-family models, sampling, production batching, or KV-cache-optimized draft/verify kernels.

## Claim scope

On GB10, a vanilla GPT-2-small checkpoint using untrained intermediate-layer unembedding does not provide enough early-layer agreement to make gamma=4 layer-skip self-speculative decoding faster than greedy decoding under the measured timing proxy.

## Why it stopped

Proxy early falsification rather than full validation: the directly tested vanilla GPT-2 intermediate unembedding path produced estimated slowdowns at every exit layer, so repeating larger vanilla probes is not justified.

## Recommended next action

Stop this vanilla-checkpoint path; run one bounded follow-up that trains or uses a checkpoint with explicit early-exit loss/layer dropout and requires measured exact-output speedup over greedy decoding before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 trained early-exit self-speculative decoding check
- Success threshold: At least 1.10x measured wall-clock speedup over greedy decoding with exact greedy-output equivalence on at least 512 generated positions, plus intermediate top-1 agreement of at least 75% at an exit layer that skips 25% or more of transformer blocks.
- Stop condition: Stop if trained early-exit top-1 agreement is below 60%, exact-output checks fail, or measured self-speculative latency remains below 1.0x greedy speed after one calibrated implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-self-speculative-decoding-on-gb10-ef1df330d006`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
