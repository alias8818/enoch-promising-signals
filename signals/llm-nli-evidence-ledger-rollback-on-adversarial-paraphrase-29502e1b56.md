# LLM/NLI evidence-ledger rollback on adversarial paraphrase contradiction traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-nli-evidence-ledger-rollback-on-adversarial-paraphrase-29502e1b56`
Run ID: `llm-nli-evidence-ledger-rollback-on-adversarial-paraphrase-29502e1b56-20260522T034134415934+0000`

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

- Parent run decision: LangGraph evidence-ledger rollback on noisy natural-language contradiction traces: enoch://control-plane/projects/langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d/runs/langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d-20260522T021912930465+0000
- Parent run decision: Evidence-ledger agent with rollback on contradiction: enoch://control-plane/projects/evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66/runs/evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66-20260521T220804590367+0000

## What looked useful

Ungated NLI over all ledger evidence is unsafe because it falsely rolls back neutral same-entity updates. Schema-gated NLI selected on seed 101 and evaluated on held-out seeds 202/303 reached F1 0.925 versus 0.859 for the lexical baseline, with paired bootstrap F1 difference 95% CI [0.036, 0.099].

## Boundaries and scale limits

Tested on 1,440 synthetic template traces with a tiny cached MNLI model; entity/attribute slots were supplied by the generator, not extracted from free-form LLM output; larger MNLI checkpoints and real paraphrase datasets were not validated.

## Claim scope

On deterministic synthetic adversarial paraphrase contradiction traces, a structured evidence-ledger that gates comparisons by entity/attribute and uses bidirectional MNLI for same-slot arbitration improves held-out rollback F1 over latest-wins and lexical value baselines.

## Why it stopped

Tier 2 local evidence supports the scoped mechanism but remains synthetic and component-oracle; this is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with non-oracle slot extraction, a stronger MNLI checkpoint, and LLM-generated or human paraphrase contradiction traces before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle slot extraction and stronger MNLI for evidence-ledger rollback
- Success threshold: On held-out traces, schema-gated NLI must improve rollback F1 by at least 0.04 over the best non-NLI baseline while keeping false rollback rate below 0.12.
- Stop condition: Stop if slot extraction errors erase the F1 advantage, if false rollback rate exceeds 0.12 at the best held-out threshold, or if the stronger NLI model does not outperform the lexical baseline.

## Evidence references

- Artifact root: `<local-path>/projects/llm-nli-evidence-ledger-rollback-on-adversarial-paraphrase-29502e1b56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
