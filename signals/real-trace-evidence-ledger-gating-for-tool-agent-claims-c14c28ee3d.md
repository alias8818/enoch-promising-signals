# Real-trace evidence-ledger gating for tool-agent claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-gating-for-tool-agent-claims-c14c28ee3d`
Run ID: `real-trace-evidence-ledger-gating-for-tool-agent-claims-c14c28ee3d-20260601T095030909877+0000`

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

- Parent run decision: Evidence-ledger tool-agent hallucination reduction: enoch://control-plane/projects/evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa/runs/evidence-ledger-tool-agent-hallucination-reduction-14efac4696fa-20260601T035540826753+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/88b7da3728d1

## What looked useful

Tier 1 direct test passed: 10 real command events, 93 claims, 37/37 supported claims accepted, 56/56 unsupported claims rejected, accept-all baseline accuracy 0.3978494623655914.

## Boundaries and scale limits

Single local trace; controlled/generated claims rather than naturally occurring final-answer claims; exact string and exit-code assertions only; no human annotation, semantic entailment, multi-agent, or multi-domain evaluation.

## Claim scope

In one real Codex tool-agent command trace with controlled claim corruptions, event-local evidence-ledger gating accepted all supported exit-code, command-substring, and output-substring claims and rejected all unsupported wrong-exit, missing-citation, altered-output, nonexistent-command, and cross-event substitution claims.

## Why it stopped

No-paper useful signal: the controlled real-trace mechanism test met threshold, but claim generation was synthetic/controlled and too narrow for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on 20 real tool-agent traces with human-labeled natural-language claims and compare ledger gating against citation-only and accept-all baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-labeled natural-claim benchmark for real-trace evidence-ledger gating
- Success threshold: Reject at least 85% of human-labeled unsupported claims with at least 90% recall on supported claims, and outperform citation-only gating by at least 20 percentage points in unsupported rejection rate.
- Stop condition: Stop if fewer than 20 usable real traces with natural final claims are available, or if unsupported rejection is below 70% after annotation of the first 10 traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-gating-for-tool-agent-claims-c14c28ee3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
