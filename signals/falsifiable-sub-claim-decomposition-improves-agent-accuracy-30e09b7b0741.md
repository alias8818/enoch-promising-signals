# Falsifiable Sub-Claim Decomposition Improves Agent Accuracy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `falsifiable-sub-claim-decomposition-improves-agent-accuracy-30e09b7b0741`
Run ID: `falsifiable-sub-claim-decomposition-improves-agent-accuracy-30e09b7b0741-20260525T192241078445+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/12cd6f3c96f9

## What looked useful

Decomposition helped only with near-oracle subclaim extraction: at 0% extraction error it averaged +3.943 percentage points over direct verification, but at 5% extraction error it averaged -1.353 points and at 10% or more it lost in every condition. This suggests falsifiable decomposition is fragile unless extraction precision is very high.

## Boundaries and scale limits

No real LLM, natural-language parser, retrieval system, tool-use cost, or public benchmark was run. Results are a controlled mechanism probe, not a full validation of agent accuracy in deployed systems.

## Claim scope

Synthetic conjunctive fact-verification tasks with a stochastic verifier-agent; decomposition means independently validating 3-8 atomic subclaims and accepting only when all pass.

## Why it stopped

Proxy evidence is mixed and fragile: it supports a mechanism only under oracle extraction and does not validate the broad agent-accuracy claim.

## Recommended next action

Stop paper progression for this run; run a bounded real-LLM deepen test on a multi-hop QA or fact-verification benchmark with direct, model-decomposed, and oracle-decomposed arms.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM Decomposition Accuracy Versus Extraction Error
- Success threshold: Model-generated decomposition beats direct answering by at least 5 percentage points with paired 95% confidence interval above zero, while oracle decomposition shows the expected upper-bound gain.
- Stop condition: Stop if model-generated decomposition fails to beat direct answering or if measured extraction accuracy is below the threshold needed for a positive final-answer delta.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-sub-claim-decomposition-improves-agent-accuracy-30e09b7b0741`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
