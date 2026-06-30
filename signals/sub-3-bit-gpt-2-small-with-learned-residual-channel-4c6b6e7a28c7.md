# Sub-3-bit GPT-2-small with Learned Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-3-bit-gpt-2-small-with-learned-residual-channel-4c6b6e7a28c7`
Run ID: `sub-3-bit-gpt-2-small-with-learned-residual-channel-4c6b6e7a28c7-20260620T072452335185+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a258cba71a72

## What looked useful

No-residual 2-bit projection quantization collapsed GPT-2-small validation loss to 35.8174. A rank-4 residual channel improved from 12.7881 initial loss to 5.4587 after 120 steps at 2.111 effective projection bits, but full precision was 4.0583, so the mechanism is useful but not paper-ready.

## Boundaries and scale limits

Only projection tensors were quantized; embeddings and layer norms were not included in compressed-model accounting. Evaluation used 128 validation blocks at sequence length 128, adaptation used 512 training blocks and 120 steps, with one seed and no rank/budget sweep.

## Claim scope

Bounded GPT-2-small projection-weight probe on 128 WikiText-2 validation blocks: 2-bit affine projection quantization plus a rank-4 learned residual channel at 2.111 effective bits/projection-weight recovers much of a collapsed quantized model but does not match full precision.

## Why it stopped

Bounded direct probe found a useful recovery mechanism but not enough quality preservation for a paper-ready positive result.

## Recommended next action

Run a bounded deepen test with rank 8/16 residual channels, longer adapter training, and a matched quantization baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rank and adaptation-budget sweep for sub-3-bit GPT-2-small residual quantization
- Success threshold: A sub-3-bit projection model reaches within 0.3 validation-loss nats of full precision on a larger held-out WikiText-2 slice and beats a 3-bit no-residual baseline at similar or lower effective storage.
- Stop condition: Stop if rank 16 with at least 1000 residual-only steps remains more than 0.7 validation-loss nats worse than full precision or fails to beat the matched 3-bit no-residual baseline.

## Evidence references

- Artifact root: `<local-path>/projects/sub-3-bit-gpt-2-small-with-learned-residual-channel-4c6b6e7a28c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
