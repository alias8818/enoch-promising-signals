# Evidence-ledger loop on a public fact-verification dataset

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-loop-on-a-public-fact-verification-dataset-f58e3b0333`
Run ID: `evidence-ledger-loop-on-a-public-fact-verification-dataset-f58e3b0333-20260530T044733795672+0000`

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

- Parent run decision: Evidence-ledger agent loop on CPU: enoch://control-plane/projects/evidence-ledger-agent-loop-on-cpu-1e2d770f944c/runs/evidence-ledger-agent-loop-on-cpu-1e2d770f944c-20260530T002811149670+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Ledger top-3 raised rationale hit rate from 0.3195 to 0.5917, but macro-F1 fell from 0.3367 to 0.3309. Oracle gold rationales reached only 0.3383 macro-F1, indicating verdict scoring/aggregation rather than evidence coverage was the bottleneck.

## Boundaries and scale limits

Small controlled direct test on 338 SciFact dev claim-doc instances using cited abstracts only; not open-corpus retrieval, not large-model reasoning, and not a learned multi-sentence verifier.

## Claim scope

On SciFact dev claim+cited-abstract SUPPORT/CONTRADICT instances, this lightweight TF-IDF retrieval plus logistic-regression evidence-ledger loop increases gold-rationale coverage but does not improve verdict macro-F1 over a single top-1 evidence decision.

## Why it stopped

Controlled small direct test failed the pre-set verdict macro-F1 threshold; this is an early no-paper falsification for the lightweight ledger implementation, not a full validation of all evidence-ledger designs.

## Recommended next action

Run one bounded deepen follow-up replacing the lightweight sentence scorer with a frozen NLI/verifier or learned multi-sentence aggregator on the same SciFact protocol; stop if higher rationale coverage still fails to produce at least +0.05 macro-F1.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger verdict aggregation with a stronger verifier on SciFact
- Success threshold: ledger_top3 or learned ledger aggregation macro-F1 >= single_top1 macro-F1 + 0.05 with rationale hit rate not lower than single_top1, and oracle-rationale macro-F1 materially above single_top1.
- Stop condition: Stop as negative if the stronger verifier's ledger top-3 macro-F1 improves by less than 0.02 or oracle-rationale macro-F1 remains within 0.02 of single_top1.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-loop-on-a-public-fact-verification-dataset-f58e3b0333`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
