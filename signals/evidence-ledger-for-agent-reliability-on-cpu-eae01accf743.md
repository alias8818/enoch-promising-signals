# Evidence Ledger for Agent Reliability on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-agent-reliability-on-cpu-eae01accf743`
Run ID: `evidence-ledger-for-agent-reliability-on-cpu-eae01accf743-20260527T153843164558+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06b6c0b34725

## What looked useful

Evidence ledgers can make agent reliability measurable as a precision/coverage tradeoff: the verifier eliminated tested false accepts at negligible CPU cost but reduced coverage to 16.67% by rejecting unsupported or incomplete outputs.

## Boundaries and scale limits

Synthetic tasks and simulated agent failure modes only; no real LLM/tool agent, no natural-language evidence extraction, no long-horizon or adversarial real-world workflow validation.

## Claim scope

In a 6,000-episode deterministic synthetic benchmark with machine-checkable contexts, a structured evidence ledger plus verifier reduced false accepted answers from 33.33% under raw acceptance to 0.00%, while accepting only complete and derivable ledgers.

## Why it stopped

Synthetic verifier-defined evidence supports the mechanism but is not direct full validation of agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded real-agent benchmark that measures whether ledger requirements preserve enough coverage on natural-language tool tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Coverage and False-Accept Probe
- Success threshold: Ledger gating cuts false accepted answers by at least 50% relative to raw acceptance with accepted accuracy at least 95% and coverage at least 50% on 100 or more real-agent episodes.
- Stop condition: Stop if coverage is below 30% or accepted accuracy is below 90%, because the ledger requirement would not yet be practically reliable.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-agent-reliability-on-cpu-eae01accf743`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
