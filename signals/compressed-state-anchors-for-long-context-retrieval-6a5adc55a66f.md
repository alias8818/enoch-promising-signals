# Compressed State Anchors for Long-Context Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-anchors-for-long-context-retrieval-6a5adc55a66f`
Run ID: `compressed-state-anchors-for-long-context-retrieval-6a5adc55a66f-20260613T065328451259+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6db3840ff63f

## What looked useful

On 128 CUDA trials with 256 chunks x 256 tokens, one full-dimensional top-norm anchor per chunk achieved 1.000 target-chunk recall while scanning 0.39% of chunks; mean pooling reached 0.180 recall at top-8 and random 16-anchor retrieval reached 0.062. With zero salience, top-norm recall collapsed to 0.016.

## Boundaries and scale limits

No real transformer hidden states, no natural language corpus, no trained model integration, no KV-cache implementation, and no answer-generation evaluation. Low-dimensional random projection reduced recall, and non-salient states were not recovered.

## Claim scope

Synthetic state-vector retrieval only: top-norm compressed state anchors can preserve norm-salient needle states and shortlist the correct chunk at very low scan fraction.

## Why it stopped

Proxy-only useful signal with a clear boundary condition; not publication-grade evidence for long-context model retrieval.

## Recommended next action

Run a bounded deepen experiment on real small-transformer hidden states using the same anchor policies and report chunk recall plus answer recovery after local exact scan.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Hidden-State Test for Compressed State Anchors
- Success threshold: At <=1% stored scalar-state budget and <=3.125% chunk scan fraction, top-norm anchors improve target chunk recall by at least 3x over mean pooling and recover at least 80% of full-scan answer accuracy.
- Stop condition: Stop if top-norm anchors fail to beat mean pooling by 2x on chunk recall or if answer recovery is below 50% of full-scan accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-anchors-for-long-context-retrieval-6a5adc55a66f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
