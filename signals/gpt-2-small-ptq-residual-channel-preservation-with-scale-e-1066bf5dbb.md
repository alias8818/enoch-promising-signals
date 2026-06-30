# GPT-2-small PTQ residual-channel preservation with scale exclusion

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-ptq-residual-channel-preservation-with-scale-e-1066bf5dbb`
Run ID: `gpt-2-small-ptq-residual-channel-preservation-with-scale-e-1066bf5dbb-20260613T115534092347+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 2-bit PTQ with residual channel preservation on gb10: enoch://control-plane/projects/2-bit-ptq-with-residual-channel-preservation-on-gb10-c7e82cd76bfb/runs/2-bit-ptq-with-residual-channel-preservation-on-gb10-c7e82cd76bfb-20260613T110544656301+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b2e9f148a6b9

## What looked useful

Scale-included outlier preservation barely improved loss delta versus all-channel int4 (3.9593 vs 4.0238), while scale-excluded outlier preservation reduced loss delta to 0.2238 at 2% preserved channels and beat random preserved channels. 1%, 2%, and 4% preserved-channel ablations all met the predeclared threshold.

## Boundaries and scale limits

Tested only openai-community/gpt2, short 128-token windows, 6096 evaluation tokens for the main run, one dataset split, Python forward hooks, residual block-output activation quantization only, no weight/KV quantization, no production kernel or full-corpus validation.

## Claim scope

In a Tier 1 GPT-2-small inference test on WikiText-2 test slices, preserving calibrated residual-stream outlier channels during int4 activation PTQ helps substantially only when those preserved channels are excluded from the shared per-token quantization scale.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is not broad or robust enough for publication readiness.

## Recommended next action

Run a bounded deepen validation on full WikiText-2 with at least one additional GPT-2/Pythia-class model, per-layer and per-bit ablations, and a realistic quantization implementation before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-split GPT-2/Pythia residual scale-exclusion PTQ validation
- Success threshold: Scale-excluded outlier preservation must reduce loss degradation by at least 25% versus all-channel activation PTQ and beat scale-included and random-channel controls on both models for at least two bit-width or preserve-fraction settings.
- Stop condition: Stop if scale-excluded preservation fails to beat scale-included preservation on full-split GPT-2-small, or if the effect only appears in the Python-hook implementation and disappears under a realistic quantization path.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-ptq-residual-channel-preservation-with-scale-e-1066bf5dbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
