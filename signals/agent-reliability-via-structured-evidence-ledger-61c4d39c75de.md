# Agent Reliability via Structured Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-structured-evidence-ledger-61c4d39c75de`
Run ID: `agent-reliability-via-structured-evidence-ledger-61c4d39c75de-20260605T103504760479+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/ffc50c4ab94f

## What looked useful

Across five seeds of 40,000 tasks each, the structured ledger had the lowest unsupported-answer rate (0.0371 mean) and highest accuracy when answered (0.9477 mean), but lower end-to-end accuracy (0.7964 mean) than source-weighted no-abstain (0.8638 mean) because it abstained on about 16.65% of cases.

## Boundaries and scale limits

Synthetic binary claims only; no natural-language parsing, real retrieval corpus, LLM agent loop, human grading, latency/token overhead, or production workflow validation.

## Claim scope

In a deterministic synthetic evidence-packet benchmark, a structured ledger policy using relevance, source quality, polarity, confidence, and contradiction-aware abstention reduced unsupported answers versus majority, confidence-only, and source-weighted always-answer controls.

## Why it stopped

Proxy-only synthetic useful signal; mechanism reduces unsupported answers but does not establish real-agent reliability and loses end-to-end accuracy versus an always-answer source-weighted control.

## Recommended next action

Stop paper path for this run; run a bounded LLM-agent deepen benchmark before making any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent evidence ledger benchmark with adversarial retrieved documents
- Success threshold: Unsupported-answer rate reduced by >=50% versus source-weighted always-answer control with <=10% relative loss in end-to-end accuracy and <=25% token overhead.
- Stop condition: Stop as negative if unsupported-answer reduction is <25%, if end-to-end accuracy loss exceeds 20%, or if grading shows ledger fields are mostly post-hoc rationalization rather than evidence-grounded decisions.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-structured-evidence-ledger-61c4d39c75de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
