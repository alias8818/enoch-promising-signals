# Prompt Lookup Decoding refinement, draft-free

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `prompt-lookup-decoding-refinement-draft-free-010c5fd6cb24`
Run ID: `prompt-lookup-decoding-refinement-draft-free-010c5fd6cb24-20260628T162741967801+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/05dbfb031094

## What looked useful

Consensus refinement reduced proposed tokens but did not improve accepted-token yield. The oracle best-candidate policy reached 0.061833 accepted tokens per position versus 0.052000 for baseline_recent, showing candidate-selection headroom even though this consensus rule failed to capture it.

## Boundaries and scale limits

Small CPU-only benchmark; regex tokenizer; prose only; no verifier model, production decoder loop, chat/code workloads, or wall-clock generation throughput measurement.

## Claim scope

A simple draft-free consensus/reranking refinement for prompt-lookup decoding was tested offline on three public-domain prose texts using exact future-token acceptance as the target metric. It did not improve accepted tokens per position over the most-recent longest-match baseline.

## Why it stopped

Proxy/local early falsification: the tested consensus refinement did not beat the baseline on direct accepted-token metrics, so it is not viable as a paper result without a different selection rule and model-backed validation.

## Recommended next action

Stop this refinement as no-paper evidence; run one bounded follow-up that learns or hand-tunes candidate selection features against the oracle gap on held-out texts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Feature-based prompt-lookup candidate selection against oracle headroom
- Success threshold: At least 10% relative improvement in accepted tokens per position over baseline_recent with no more than 5% increase in proposed tokens per position on held-out texts.
- Stop condition: Stop if the selector cannot exceed baseline_recent by 5% relative accepted tokens per position on a development split or if scoring overhead dominates the saved verification work.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-decoding-refinement-draft-free-010c5fd6cb24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
