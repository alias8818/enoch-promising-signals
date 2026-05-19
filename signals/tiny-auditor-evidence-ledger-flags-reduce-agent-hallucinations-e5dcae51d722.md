# Tiny Auditor Evidence Ledger Flags Reduce Agent Hallucinations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-auditor-evidence-ledger-flags-reduce-agent-hallucinations-e5dcae51d722`
Run ID: `tiny-auditor-evidence-ledger-flags-reduce-agent-hallucinations-e5dcae51d722-20260518T131239604748+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f96907f28b2e

## What looked useful

The run supports the mechanism that subject-keyed evidence ledgers can flag distractor-backed unsupported claims that naive value-overlap checks accept, but only in a clean structured synthetic setting.

## Boundaries and scale limits

Synthetic profile data; exact field/value matching; 100 actual-model cases plus 200 simulated-control cases; deliberately hallucination-prone prompt; no real RAG traces, no human labels, no paraphrase or multi-hop evidence evaluation.

## Claim scope

On a synthetic evidence-grounded company-profile QA benchmark with atomic field claims, a subject-keyed evidence ledger auditor reduced accepted unsupported claims from Qwen/Qwen2.5-0.5B-Instruct outputs from 233/319 to 0/86 accepted claims, while a value-overlap control still accepted 128 unsupported claims.

## Why it stopped

Synthetic/proxy evidence supports a bounded mechanism but is not direct or broad enough for a paper-ready hallucination-reduction claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ledger auditor on 200-500 real or realistic RAG/agent answers with claim/evidence labels and citation-prompting controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger auditor on labeled RAG or agent traces
- Success threshold: Accepted unsupported claim rate reduced by at least 50% versus raw acceptance and at least 25% versus the strongest baseline, with supported-claim false-flag rate at or below 10%.
- Stop condition: Stop if the ledger auditor fails to beat the strongest baseline by 10 percentage points in accepted unsupported rate or if supported-claim false-flag rate exceeds 20%.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-auditor-evidence-ledger-flags-reduce-agent-hallucinations-e5dcae51d722`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
