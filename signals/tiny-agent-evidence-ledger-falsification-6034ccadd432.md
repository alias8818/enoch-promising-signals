# Tiny Agent Evidence Ledger Falsification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-falsification-6034ccadd432`
Run ID: `tiny-agent-evidence-ledger-falsification-6034ccadd432-20260531T134953618356+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/17ab5397eb0f

## What looked useful

Ledger verification achieved 0.99995 mean falsification recall with 1.0 honest specificity, versus 0.29350 mean recall for answer-only checking. The only ledger miss was caused by duplicate documents containing identical supporting evidence.

## Boundaries and scale limits

Synthetic templated facts and deterministic falsification modes only; no real LLM traces, natural paraphrase, retrieval errors, signed append-only ledger, or adversarial ledger tampering were tested.

## Claim scope

In a deterministic synthetic document-QA harness with 25,000 tiny-agent outputs, a simple evidence ledger verifier caught provenance and quote falsification modes that final-answer-only checking missed.

## Why it stopped

No-paper closure: this is proxy/synthetic evidence supporting the mechanism, not full validation on real agents or adversarial ledgers.

## Recommended next action

Stop this run as a synthetic useful signal; run a bounded follow-up on real tiny-agent traces with labeled citation support and duplicate-document policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Evidence Ledger Falsification Check
- Success threshold: Ledger falsification recall exceeds answer-only recall by >=0.30 absolute with honest specificity >=0.95 on labeled natural traces.
- Stop condition: Stop if ledger recall lift is <0.10 absolute, honest specificity is <0.90, or most failures require semantic support beyond quote/provenance checking.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-falsification-6034ccadd432`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
