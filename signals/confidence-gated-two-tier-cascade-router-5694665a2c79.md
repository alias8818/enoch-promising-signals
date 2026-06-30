# Confidence-Gated Two-Tier Cascade Router

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-two-tier-cascade-router-5694665a2c79`
Run ID: `confidence-gated-two-tier-cascade-router-5694665a2c79-20260621T121802243290+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6677ab870bb4

## What looked useful

Confidence gating beat random matched escalation and preserved strong-model accuracy within 0.4 percentage points, but near-strong quality required about 90% escalation and was 2.58% more expensive than direct strong-tier inference at an 8:1 cost ratio. The proxy becomes cost-positive when quality tolerance is relaxed or the strong/cheap cost ratio exceeds the measured break-even.

## Boundaries and scale limits

No real LLM prompts, no production traces, no token latency, no calibration drift, and no full serving benchmark. The result only tests the routing mechanism and cost-quality trade-off in a controlled proxy.

## Claim scope

Synthetic proxy classification benchmark with a cheap linear tier, stronger MLP tier, validation-selected max-softmax confidence gate, and normalized tier costs of 1.0 cheap and 8.0 strong.

## Why it stopped

Proxy evidence supports the confidence-gating mechanism but not a near-strong quality cost win at the tested 8:1 tier cost ratio; synthetic-only evidence is insufficient for a paper-positive claim.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use real small/large model outputs or production-like LLM traces to measure whether confidence separates answerable prompts strongly enough to beat the 12.7x near-strong break-even ratio.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based LLM Cascade Break-Even Test
- Success threshold: At <=1 percentage point quality loss versus direct strong-model inference, show positive cost reduction versus direct strong inference and at least 2 percentage points quality gain over random matched escalation.
- Stop condition: Stop if confidence-gated routing cannot beat random matched escalation or if the break-even strong/cheap cost ratio remains above realistic deployment ratios for the tested models.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-two-tier-cascade-router-5694665a2c79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
