# LLM Agent Evidence-Ledger Gate Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-agent-evidence-ledger-gate-test-aebc52e098`
Run ID: `llm-agent-evidence-ledger-gate-test-aebc52e098-20260524T235228082550+0000`

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

- Parent run decision: Evidence-Ledger Constrained Agent Tool Use: enoch://control-plane/projects/evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d/runs/evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d-20260524T234243007240+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5293e1f994e2

## What looked useful

The deterministic evidence-ledger gate rejected 31/31 unsupported controlled packages and accepted 6/6 valid controls, meeting the preset threshold of at least 90% unsupported rejection with at most 10% false rejects.

## Boundaries and scale limits

No live LLM agents, no natural transcript claim extraction, no blind human adjudication, no adaptive adversarial testing, and no production controller integration were tested.

## Claim scope

Tier 1 controlled small direct test of an evidence-ledger gate on 37 filesystem-backed Enoch-like decision packages with explicit valid controls and injected unsupported-closure failures.

## Why it stopped

No-paper useful signal: the controlled direct gate mechanism passed, but the evidence is local synthetic package validation rather than real-agent transcript validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen test on at least 30 real or replayed agent transcript packages with blind labels for supported versus unsupported closures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Transcript Evidence-Ledger Gate
- Success threshold: Reject at least 90% of blindly labeled unsupported closures with at most 10% false rejects on labeled valid closures.
- Stop condition: Stop if unsupported-closure recall is below 80% or valid-closure false reject rate exceeds 20%, because the mechanism would be too brittle for controller gating.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-evidence-ledger-gate-test-aebc52e098`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
