# INT1 Weights plus FP16 KV Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int1-weights-plus-fp16-kv-residual-channel-980f23370362`
Run ID: `int1-weights-plus-fp16-kv-residual-channel-980f23370362-20260527T030513208726+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ed176a8ddba3

## What looked useful

FP16 K/V residual channels monotonically improve agreement with full-precision attention, but small channel counts provide negligible recovery: 1-8 channels reduce attention-core relative MSE by only 0.25%-1.69% and post-output MSE by 0.14%-0.90%. Meaningful recovery needs large overhead, e.g. 128 channels costs 8x INT1 KV-cache storage and still leaves post-output relative MSE at 0.678; full 256-channel residual costs 16x and still leaves 0.564 post-output relative MSE because Q/O INT1 errors remain.

## Boundaries and scale limits

No pretrained language-model perplexity, no finetuning, no learned residual policy, no hardware kernel, and no long-context serving validation. The result directly tests the local K/V residual mechanism but not full model quality.

## Claim scope

Synthetic attention-projection probe of signed INT1 Q/K/V/O weights with selected FP16 K/V residual activation channels at batch 4, sequence 256, hidden dimension 256, 8 heads, and 16 random seeds.

## Why it stopped

Early bounded mechanism test is mixed but negative for the small FP16 KV residual channel hypothesis: recovery is monotonic, yet too weak at low overhead and dominated by remaining INT1 Q/O errors. This is a proxy/mechanism result, not full language-model validation.

## Recommended next action

Stop this line as a paper claim; only revisit with a direct pretrained small-transformer perplexity experiment that compares <=25% KV residual overhead against matched-memory INT2/INT4 or Q/O residual baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-memory pretrained small-transformer KV residual test
- Success threshold: Recommend continuing only if <=25% FP16 K/V residual overhead recovers at least 20% of pure INT1 perplexity degradation over full precision and beats matched-memory INT2/INT4 or Q/O-residual controls.
- Stop condition: Stop if <=25% K/V residual overhead recovers less than 10% of pure INT1 perplexity degradation or loses to matched-memory baselines.

## Evidence references

- Artifact root: `<local-path>/projects/int1-weights-plus-fp16-kv-residual-channel-980f23370362`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
