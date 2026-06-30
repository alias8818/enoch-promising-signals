# Evidence-Ledger vs Adversarial Prompt Injection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-vs-adversarial-prompt-injection-7ed6629c6aa4`
Run ID: `evidence-ledger-vs-adversarial-prompt-injection-7ed6629c6aa4-20260611T062948706498+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb94e1342f57

## What looked useful

The useful mechanism is provenance-gated ledger admission, not the presence of a ledger alone: the unsafe ledger that parsed untrusted fact-looking records failed at the same rate as the naive injected reader.

## Boundaries and scale limits

720 synthetic cases across 3 seeds; no real LLM, real RAG corpus, adaptive attack search, or production retrieval stack was evaluated.

## Claim scope

In a deterministic synthetic document-grounded QA harness, a provenance-gated evidence ledger prevented injected instructions and forged fact-looking records from affecting answers, while naive context reading and an unsafe ledger ablation were fully compromised.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not full validation of real LLM prompt-injection robustness.

## Recommended next action

Stop this run as no-paper useful signal; next run should wrap a small real instruction-following model or API model with the same provenance-gated ledger and evaluate on a public RAG prompt-injection benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model RAG Prompt-Injection Test for Provenance-Gated Evidence Ledgers
- Success threshold: At least 50 percentage-point attack-success reduction versus naive RAG with clean accuracy within 5 percentage points of naive clean performance and no comparable failure in the unsafe-ledger ablation.
- Stop condition: Stop if the ledger reduces clean accuracy by more than 10 percentage points, fails to reduce attack success by at least 25 percentage points, or cannot preserve citation faithfulness under schema-compatible poisoning.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-vs-adversarial-prompt-injection-7ed6629c6aa4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
