# Evidence Ledger for Tiny Tool Agents on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-tool-agents-on-cpu-c3979fd4e4fe`
Run ID: `evidence-ledger-for-tiny-tool-agents-on-cpu-c3979fd4e4fe-20260602T181650793271+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b67010670af1

## What looked useful

Ledger validation changed failures from unsupported confident answers to abstentions; with one retry, five-seed mean coverage was 0.92632, answered accuracy was 1.0, unsupported task rate fell from 0.38324 to 0.07368, and tool-call overhead was 1.169x.

## Boundaries and scale limits

Tested only on synthetic fact-table tasks: 5,000-task main run plus five-seed retry sweep, no natural-language claim extraction, no real external tools, no adversarial provenance forgery, no larger agent planning benchmark.

## Claim scope

In a deterministic synthetic CPU benchmark of tiny aggregate-answer tool agents with labeled missing/corrupt/stale/ok tool observations, an append-only evidence ledger plus strict support validation eliminated wrong answered claims and traded abstention/retry overhead for higher grounded accuracy.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but does not validate real tool-agent evidence grounding or natural-language claim auditing.

## Recommended next action

Stop this run as no-paper useful signal; next run should test ledger support checking on natural-language tool snippets with adversarial evidence and a citation-prompt baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language evidence ledger for adversarial tiny tool agents
- Success threshold: At least 25 percentage-point reduction in unsupported emitted claims versus citation-prompt baseline at no more than 20 percentage-point coverage loss and no more than 2x absolute CPU runtime on 5,000+ examples.
- Stop condition: Stop if ledger support checking fails to reduce unsupported emitted claims by at least 10 percentage points or if coverage drops below 60% under non-adversarial noisy snippets.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-tool-agents-on-cpu-c3979fd4e4fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
