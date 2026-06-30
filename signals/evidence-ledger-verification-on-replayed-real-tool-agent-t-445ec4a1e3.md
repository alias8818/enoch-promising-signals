# Evidence-ledger verification on replayed real tool-agent transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-verification-on-replayed-real-tool-agent-t-445ec4a1e3`
Run ID: `evidence-ledger-verification-on-replayed-real-tool-agent-t-445ec4a1e3-20260620T223901452901+0000`

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

- Parent run decision: Evidence-Ledger Agent on Reproducible Tool Tasks: enoch://control-plane/projects/evidence-ledger-agent-on-reproducible-tool-tasks-f4f1cbad0b94/runs/evidence-ledger-agent-on-reproducible-tool-tasks-f4f1cbad0b94-20260620T222833578031+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8478ec7cb8b7

## What looked useful

Tier 1 direct replay test met the exact threshold: 6/6 claims classified correctly, with 0 false accepts and 0 false rejects over explicit evidence ID and field/value requirements.

## Boundaries and scale limits

Single small local transcript with claims pinned to explicit evidence item IDs, 6 hand-authored claims, 2 positive controls, 4 planted negative controls; no multi-agent corpus, automated claim extraction, adversarial paraphrase robustness, or baseline comparison.

## Claim scope

A deterministic evidence-ledger verifier can correctly accept and reject a small hand-authored claim set against one replayed real local Codex tool-agent transcript.

## Why it stopped

Useful Tier 1 mechanism signal only; one-transcript controlled replay is not broad or publication-grade validation.

## Recommended next action

Run a bounded deepen test on 20-50 real tool-agent transcripts with extracted claims and compare against an unstructured transcript-search baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-level evidence-ledger verification on replayed tool-agent transcripts
- Success threshold: Evidence-ledger verifier has lower false_accept_rate than baseline by at least 50 percent with false_reject_rate no worse than baseline plus 5 percentage points.
- Stop condition: Stop if false_accept_rate is not lower than baseline, if false_reject_rate exceeds baseline by more than 5 percentage points, or if claim labeling cannot be made reproducible.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-verification-on-replayed-real-tool-agent-t-445ec4a1e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
