# Predictive Operator Model from Trace Compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `predictive-operator-model-from-trace-compression-cf312689bebe`
Run ID: `predictive-operator-model-from-trace-compression-cf312689bebe-20260613T053521963433+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b47ae733d08

## What looked useful

The compressed-prefix model was predictive but did not beat simple baselines in the regimes most favorable to phrase structure: motif accuracy was 0.7642 versus 0.8917 raw-window and 0.8472 3-gram; callstack accuracy was effectively tied at 0.6203 versus 0.6216 raw-window and 0.6200 3-gram. Its only win was a tiny Markov gain of +0.0020 over raw-window.

## Boundaries and scale limits

CPU-only synthetic benchmark; 3 seeds per regime; no real execution traces; no learned neural compressor; no GPT-2-scale or production workload validation.

## Claim scope

Synthetic held-out next-operator prediction for IID, Markov, motif, and callstack-like traces using an LZ78-style compressed-prefix feature MLP compared with unigram, 3-gram, and raw recent-window MLP baselines.

## Why it stopped

Synthetic proxy evidence did not support a baseline-beating predictive operator model from LZ-style trace compression; this is not a full validation of all compression approaches.

## Recommended next action

Stop this run as a proxy early falsification; a new bounded deepen test should use real operator traces and a direct compressed-state predictor before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct compressed-state predictors on real operator traces
- Success threshold: Compressed-state predictor beats every baseline by at least 5 absolute accuracy points or at least 10% lower NLL on most workloads, with no regression on IID/control traces.
- Stop condition: Stop if the compressed-state predictor fails to beat raw-window and n-gram baselines on motif/callstack controls and at least one real-trace workload.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-model-from-trace-compression-cf312689bebe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
