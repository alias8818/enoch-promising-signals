# Labeled Semantic Audit Benchmark for Real Tool-Calling Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `labeled-semantic-audit-benchmark-for-real-tool-calling-evi-a09edd1f2d`
Run ID: `labeled-semantic-audit-benchmark-for-real-tool-calling-evi-a09edd1f2d-20260527T001113300641+0000`

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

- Parent run decision: Evidence Ledger on Real Small Tool-Calling Traces: enoch://control-plane/projects/evidence-ledger-on-real-small-tool-calling-traces-7c40e260a3/runs/evidence-ledger-on-real-small-tool-calling-traces-7c40e260a3-20260525T213450637691+0000
- Parent run decision: Evidence Ledger for Small Tool-Calling Agents: enoch://control-plane/projects/evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f/runs/evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f-20260525T205411106069+0000

## What looked useful

Tier 2 fixed-seed evaluation met the preset threshold: semantic auditor F1 1.000 versus BM25 F1 0.842, token-overlap F1 0.822, no-entity F1 0.811, no-number F1 0.804, and shuffled-ledger F1 0.006. Mutation analysis showed 1.000 semantic accuracy on supported, entity-swap, wrong-number, wrong-date, and wrong-time cases.

## Boundaries and scale limits

The benchmark uses 3,000 generated examples across five fixed seeds and six local tool schemas. Claims are template-shaped, labels are synthetic, and the primary auditor has hand-written parsers for these claim formats. No production assistant traces, human labels, LLM paraphrases, unknown tools, or stronger NLI/LLM judge baselines were tested.

## Claim scope

On a deterministic generated benchmark of executable local tool-call evidence ledgers, a ledger-aware field-matching semantic auditor classifies supported versus unsupported claims better than BM25 and token-overlap baselines.

## Why it stopped

No-paper useful signal: the Tier 2 threshold was met, but the evidence is generated and parser-matched rather than broad real-trace validation.

## Recommended next action

Stop paper escalation for this run; next useful bounded action is to build a held-out real/paraphrased ledger corpus and compare the same audit protocol against NLI and LLM-as-judge baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-Out Real and Paraphrased Tool-Ledger Audit Benchmark
- Success threshold: Mean F1 >= 0.85 across at least three fixed seeds or folds, and >= 0.10 F1 improvement over the strongest non-oracle baseline, with shuffled-ledger F1 near chance.
- Stop condition: Stop if the auditor fails to beat the strongest baseline by 0.05 F1 on the first 200 labeled held-out examples or if labels cannot be produced without private/external evidence.

## Evidence references

- Artifact root: `<local-path>/projects/labeled-semantic-audit-benchmark-for-real-tool-calling-evi-a09edd1f2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
