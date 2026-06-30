# Evidence-ledger agent: verifiable claims vs ungrounded baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-verifiable-claims-vs-ungrounded-baseline-65d4d8305ff1`
Run ID: `evidence-ledger-agent-verifiable-claims-vs-ungrounded-baseline-65d4d8305ff1-20260621T055004787849+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/72aaddea9ab3

## What looked useful

The benchmark found 0.9918 verifiable-supported claim rate for the evidence-ledger agent versus 0.0000 for the ungrounded baseline in the main run; the ledger also retained 0.9918 support when the baseline had perfect memory but no citations.

## Boundaries and scale limits

No production LLM, open-web retrieval, adversarial evidence, human evaluation, latency/cost analysis, or broad-domain validation was tested.

## Claim scope

In a deterministic closed-world synthetic benchmark with clean local evidence records, an evidence-ledger answerer produced far more verifiably supported claims than an ungrounded baseline.

## Why it stopped

Closed as no-paper useful signal because the result is a synthetic mechanism validation, not a full production-agent or publication-grade validation.

## Recommended next action

Run a bounded real-LLM follow-up using the same claim-level ledger metrics with local/open model answers, distractor evidence, and spot-audited claim extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM evidence-ledger evaluation with distractor evidence
- Success threshold: Evidence-ledger condition improves verifiable-supported claim rate by at least 25 percentage points and cuts unsupported/wrong emitted claims by at least 50% versus ungrounded mode, with claim recall no more than 15 percentage points lower.
- Stop condition: Stop if the ledger condition fails to reduce unsupported/wrong claims by at least 25% on the first 100 evaluated answers or if claim extraction cannot be audited reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-verifiable-claims-vs-ungrounded-baseline-65d4d8305ff1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
