# Count-Sketch + Bloom Sketch Exchange with Plausibility Gate

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `count-sketch-bloom-sketch-exchange-with-plausibility-gate-594f955a16ee`
Run ID: `count-sketch-bloom-sketch-exchange-with-plausibility-gate-594f955a16ee-20260613T015131957055+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/908164cba090

## What looked useful

The gate raised average precision by 0.1447 and reduced false positives by 17.98 candidates per trial, with average F1 gain +0.0281. The effect was strongest at width 128 with 1024 distractors (+0.2567 F1), but the same gate hurt F1 at width 128 with 64 distractors (-0.1157 F1) due to recall loss. Sketch plus Bloom payload was 4.10x to 16.10x larger than exact sparse delta exchange in the tested small-delta setting.

## Boundaries and scale limits

Synthetic only; 9 conditions x 120 trials; no real distributed protocol, no adversarial peers, no real trace corpus, no remote-only key discovery protocol, and no large-scale payload/privacy regime. CPU-only run completed in 144.669 seconds with 23,492 KB max RSS.

## Claim scope

In a bounded synthetic sparse-delta simulation with Bloom-admitted false-positive candidates, a row-consistency plus residual-reduction plausibility gate reduces false decoded deltas and improves F1 under high distractor pressure, but it trades away recall and is not communication-efficient for the tested 64-delta payload size.

## Why it stopped

Bounded synthetic evidence supports the plausibility-gate mechanism only in noisy candidate regimes and exposes recall and payload tradeoffs; this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next, implement a direct protocol-level set/state reconciliation benchmark that does not assume an external candidate pool and compare against exact sparse exchange under matched payload budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Protocol-level Count-Sketch Bloom reconciliation under matched payload budgets
- Success threshold: Under at least one predeclared non-toy regime, gated sketch exchange improves F1 by at least 0.05 over the best equal-budget baseline while keeping recall at or above 0.95 and using no more payload bits than the baseline.
- Stop condition: Stop if exact sparse exchange remains smaller and more accurate across all tested regimes, or if the gate cannot maintain recall at or above 0.95 under equal payload budgets.

## Evidence references

- Artifact root: `<local-path>/projects/count-sketch-bloom-sketch-exchange-with-plausibility-gate-594f955a16ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
