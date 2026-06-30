# Sub-byte KV cache with per-head residual projection channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-byte-kv-cache-with-per-head-residual-projection-channel-127dbfeaddb9`
Run ID: `sub-byte-kv-cache-with-per-head-residual-projection-channel-127dbfeaddb9-20260621T224103724036+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5d3a42f703b2

## What looked useful

Plain 3-bit KV quantization was the best bounded practical variant. Residual projection reduced compression ratio and degraded realistic replay metrics: in the 376-token GPT-2 run, 3-bit delta NLL rose from 0.2140 to 0.6515 and 2-bit delta NLL rose from 1.9087 to 3.2650. Oracle recompression showed only tiny residual gains, suggesting the rank-1 direction is not enough to justify extra cache state without a better cache design.

## Boundaries and scale limits

Tested GPT-2-small only, Wikitext-2 only, short 96-128 token windows, teacher-forced cached replay, no fused packing kernel, no long-context serving benchmark, and no bit-matched custom compressed-cache implementation.

## Claim scope

On GPT-2-small Wikitext cached replay, a single per-head rank-1 residual projection channel worsened realistic 2-bit and 3-bit KV-cache quantization versus plain quantization; only an oracle exact-source recompression diagnostic showed tiny improvements that are not deployment-ready.

## Why it stopped

Bounded direct replay evidence is mixed but mostly negative, and the positive oracle-only effect is too small and too proxy-like for a paper claim.

## Recommended next action

Stop this run as no-paper useful signal; the only worthwhile continuation is a bounded custom non-requantizing compressed-cache implementation with bit-matched baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-requantizing compressed KV cache with bit-matched residual projection
- Success threshold: Residual projection must improve delta NLL and KL versus the best bit-matched plain quantization baseline while retaining at least 4x fp16 cache compression and without material decode slowdown in the bounded GPT-2-small replay.
- Stop condition: Stop if residual projection fails to beat the best bit-matched plain quantization baseline on either NLL or KL, or if the implementation overhead reduces effective compression below 4x.

## Evidence references

- Artifact root: `<local-path>/projects/sub-byte-kv-cache-with-per-head-residual-projection-channel-127dbfeaddb9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
