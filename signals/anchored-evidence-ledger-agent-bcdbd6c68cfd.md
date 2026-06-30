# Anchored Evidence Ledger Agent

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchored-evidence-ledger-agent-bcdbd6c68cfd`
Run ID: `anchored-evidence-ledger-agent-bcdbd6c68cfd-20260523T142618990837+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f4aa93715e73

## What looked useful

Hash anchors are useful for span identity and tamper detection, but hash-integrity-only anchoring still false-accepted 40/80 invalid claims. The useful mechanism requires an additional claim-to-span support verifier.

## Boundaries and scale limits

Synthetic templated facts only; no live LLM, real retrieval corpus, semantic entailment model, adversarial paraphrase set, public timestamping, production latency, or multi-session agent persistence was tested.

## Claim scope

On a 40-fact synthetic retrieval-style QA corpus, a SHA-256 span ledger plus exact claim-to-span support verifier rejected fabricated citations, wrong-value claims, and post-ledger source tampering without false rejects.

## Why it stopped

Synthetic proxy evidence supports a bounded mechanism but is not full validation or paper-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the ledger into a small live RAG loop and measure natural-language unsupported-claim rejection plus supported-claim false-reject rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live RAG evidence-ledger validation on natural-language claims
- Success threshold: At least 80% reduction in unsupported false accepts versus citation-only baseline, supported-claim false-reject rate below 10%, and 100% rejection of post-ledger tampered spans in the bounded test.
- Stop condition: Stop if semantic support verification false-rejects 20% or more supported natural-language claims or if unsupported false accepts remain above 25% after anchoring and verification.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-evidence-ledger-agent-bcdbd6c68cfd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
