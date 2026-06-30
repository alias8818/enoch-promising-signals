# Layer-Skip Self-Speculation With Confidence Gated Acceptance

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-skip-self-speculation-with-confidence-gated-acceptance-b85fd6406862`
Run ID: `layer-skip-self-speculation-with-confidence-gated-acceptance-b85fd6406862-20260613T205339624023+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/600cb3951efe

## What looked useful

Auxiliary-head exit 1 at threshold 0.8 accepted 98.79% of held-out tokens with zero accuracy delta versus the final head and a 74.09% layer-cost reduction proxy. In the no-auxiliary ablation, exit 1 at threshold 0.8 accepted 92.81% of tokens but dropped gated accuracy by 37.0 percentage points, showing high confidence alone is not a safe acceptance criterion.

## Boundaries and scale limits

Synthetic task only; 4-layer 128-wide toy model; no real text, no pretrained LM, no GPT-2-small-class baseline, no KV-cache serving benchmark, and speedup is an average-layer-cost proxy rather than measured decode latency.

## Claim scope

On a synthetic noisy increment next-token task with a 4-layer toy causal transformer, confidence-gated intermediate exits can preserve final-model accuracy when the intermediate head is trained or already aligned; confidence alone can be unsafe at a too-shallow unsupervised exit.

## Why it stopped

Bounded toy evidence supports the mechanism only in a simple setting and exposes a confidence-gating failure mode; it is not full validation or publication-grade evidence.

## Recommended next action

Stop this worker run as a no-paper useful signal; next run should test exit-specific calibration on a GPT-2-small-class or pretrained small LM with real text and direct selective-risk thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Layer-Skip Acceptance on a Small Real-Text LM
- Success threshold: At least one intermediate exit accepts 25% or more tokens with less than 0.5 percentage-point accuracy loss versus the final model and at least 20% measured decode latency or validated layer-cost reduction on real text.
- Stop condition: Stop if no exit can maintain less than 1 percentage-point accuracy loss at 10% acceptance after calibration, or if measured decode overhead erases the layer-skip savings.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-self-speculation-with-confidence-gated-acceptance-b85fd6406862`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
