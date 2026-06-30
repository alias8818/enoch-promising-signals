# Non-oracle slot extraction and stronger MNLI for evidence-ledger rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `non-oracle-slot-extraction-and-stronger-mnli-for-evidence-a761861337`
Run ID: `non-oracle-slot-extraction-and-stronger-mnli-for-evidence-a761861337-20260522T042241138152+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: LangGraph evidence-ledger rollback on noisy natural-language contradiction traces: enoch://control-plane/projects/langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d/runs/langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d-20260522T021912930465+0000
- Parent run decision: LLM/NLI evidence-ledger rollback on adversarial paraphrase contradiction traces: enoch://control-plane/projects/llm-nli-evidence-ledger-rollback-on-adversarial-paraphrase-29502e1b56/runs/llm-nli-evidence-ledger-rollback-on-adversarial-paraphrase-29502e1b56-20260522T034134415934+0000

## What looked useful

MiniLM extracted-slot ledger achieved F1 0.897, contradiction leak 0.0035, and false rollback rate 0.1495 at threshold 0.55 versus lexical F1 0.758/leak 0.390/false rollback 0.0 and tiny extracted-slot F1 0.738. Holdout threshold selection preserved MiniLM extracted-slot F1 around 0.896, but same-entity distractor accuracy was only 0.5535 and oracle-slot MiniLM reached F1 0.998.

## Boundaries and scale limits

Generated templates, deterministic closed-vocabulary extractor, one stronger cached MNLI-family checkpoint, no real agent traces, no manually audited corpus, and unresolved same-entity distractor false rollbacks.

## Claim scope

On a 10,000-trace fixed-seed generated rollback benchmark with closed-vocabulary text-derived slot extraction, a stronger cached MNLI model (cross-encoder/nli-MiniLM2-L6-H768) plus extracted-slot ledger-wide NLI improves rollback F1 over lexical and tiny-MNLI controls.

## Why it stopped

No paper-positive closure: the scoped mechanism is useful, but evidence remains generated/closed-vocabulary and the non-oracle extracted-slot ledger has a large same-entity distractor false-rollback pocket.

## Recommended next action

Run one final bounded depth-4 deepen test that targets the identified same-entity distractor failure with a stricter extracted-slot pair gate or independent slot extractor, requiring false rollback below 5% while keeping contradiction leak below 5%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mitigate same-entity distractor false rollbacks in non-oracle evidence-ledger NLI
- Success threshold: False rollback rate below 0.05, contradiction leak rate below 0.05, F1 at least 0.88, and same-entity distractor condition accuracy at least 0.95 on held-out seeds.
- Stop condition: Stop if stricter gating cannot reduce false rollback below 0.10 without pushing contradiction leak above 0.10, or if the only remaining improvement requires external/manual corpus collection outside the worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/non-oracle-slot-extraction-and-stronger-mnli-for-evidence-a761861337`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
