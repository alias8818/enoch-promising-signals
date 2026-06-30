# Tool-call evidence ledger reduces unverified claims in tiny CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-call-evidence-ledger-reduces-unverified-claims-in-tiny-cpu-agents-eb48e52c60d1`
Run ID: `tool-call-evidence-ledger-reduces-unverified-claims-in-tiny-cpu-agents-eb48e52c60d1-20260528T211344026230+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2bfc7b76631e

## What looked useful

Recording a ledger alone did not change behavior; using the ledger to gate final claims eliminated unsupported and false emitted claims in all tested synthetic settings, with a measurable coverage cost that grew as retrieval coverage fell and baseline guessing rose.

## Boundaries and scale limits

Synthetic policy agent only; no real LLM, natural-language claim extraction, fuzzy entailment, noisy retrieval, multi-hop evidence, or human verification. The checker has exact structured access to claims and ledger facts, so this is mechanism evidence rather than deployment evidence.

## Claim scope

In a controlled synthetic fact-answering benchmark with a stochastic tiny CPU-local agent and exact structured claim/evidence triples, a tool-call evidence ledger used by an output checker reduced unverified emitted claims from 23.75% to 0.00% in the 10,000-task paired run, while reducing coverage from 87.26% to 68.77%.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy mechanism evidence, not direct publication-grade validation on real tiny language-model agents.

## Recommended next action

Run a bounded real-model follow-up on a small local or API-backed instruction model with natural-language tasks, comparing prompt-only citations, ledger record-only, and ledger-plus-checker using an auditable unsupported-claim scorer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language ledger checking for small instruction agents
- Success threshold: Ledger-plus-checker reduces unsupported emitted claims by >=50% versus prompt-only citation baseline and preserves >=75% of baseline correct supported claims.
- Stop condition: Stop if unsupported-claim reduction is below 25%, checker false blocks exceed 20% of supported claims, or the model cannot reliably produce parseable claims/citations after a bounded prompt repair.

## Evidence references

- Artifact root: `<local-path>/projects/tool-call-evidence-ledger-reduces-unverified-claims-in-tiny-cpu-agents-eb48e52c60d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
