# Evidence Ledger: Direct Counterexample Test for Agent Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-direct-counterexample-test-for-agent-claims-5cb48b1091dc`
Run ID: `evidence-ledger-direct-counterexample-test-for-agent-claims-5cb48b1091dc-20260620T100102188282+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c84521348d45

## What looked useful

The ledger caught 8/8 false claims and preserved 7/7 true claims, while an accept-all baseline falsely accepted 8/8 false claims. This supports the mechanism but not a broad agent-evaluation claim.

## Boundaries and scale limits

Synthetic toy corpus only; no natural-language claim extraction, real LLM transcript labeling, adversarial phrasing, multi-step provenance, or large repository diversity was tested.

## Claim scope

A deterministic local evidence ledger with artifact-specific direct counterexample probes can catch false claims in a 15-claim synthetic corpus covering files, logs, metrics, command exits, required text, and decision enum validation.

## Why it stopped

The result is a bounded synthetic/local mechanism validation, not direct/full validation on real agent transcripts.

## Recommended next action

Stop this run as no-paper useful-signal evidence; deepen with a real-transcript labeled corpus before making broader claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transcript Evidence-Ledger Counterexample Evaluation
- Success threshold: False accept rate at least 50% lower than baselines and false reject rate <= 0.10 on the labeled real-transcript corpus.
- Stop condition: Stop if referenced artifacts are unavailable for more than 30% of claims or if false reject rate exceeds 0.20 after probe fixes for obvious parser errors.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-direct-counterexample-test-for-agent-claims-5cb48b1091dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
