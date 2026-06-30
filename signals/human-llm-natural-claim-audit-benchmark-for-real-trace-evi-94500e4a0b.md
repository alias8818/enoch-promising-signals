# Human/LLM natural-claim audit benchmark for real trace evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `human-llm-natural-claim-audit-benchmark-for-real-trace-evi-94500e4a0b`
Run ID: `human-llm-natural-claim-audit-benchmark-for-real-trace-evi-94500e4a0b-20260611T061238894261+0000`

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

- Parent run decision: Append-only evidence ledgers for agent reliability audits: enoch://control-plane/projects/append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463/runs/append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463-20260611T052151856187+0000
- Parent run decision: Real-trace evidence ledger audit benchmark: enoch://control-plane/projects/real-trace-evidence-ledger-audit-benchmark-2ea74178ab/runs/real-trace-evidence-ledger-audit-benchmark-2ea74178ab-20260611T055221843457+0000

## What looked useful

Structured ledger auditing achieved 1.000 accuracy and 1.000 evidence recall across all seeds, while a retrieval-only baseline matched majority accuracy at 0.5278 and a corrupted-ledger structured control fell to 0.4750 accuracy and 0.0451 F1. This supports the benchmark mechanism but not a paper-ready Human/LLM claim.

## Boundaries and scale limits

Tested on one public git repository, 499 non-merge file-touching commits, 174 files, 720 generated template claims, and fixed seeds 11/22/33. No human auditors, no real LLM auditors, no paraphrase robustness, and no non-git ledgers were evaluated.

## Claim scope

A deterministic harness can generate answerable natural-language audit claims from a real git trace ledger, and claim truth depends on real ledger relations rather than label artifacts or token presence for the tested template grammar.

## Why it stopped

No-paper useful signal: this run validates generated trace-ledger claim answerability and evidence dependence, but the Human/LLM natural-claim benchmark claim still lacks real human/LLM auditor evidence and paraphrase robustness.

## Recommended next action

Run a bounded deepen study with real LLM and human auditors on the same labels plus paraphrased variants, measuring answer accuracy, evidence citation precision/recall, calibration, and cost/latency against the structured oracle and retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human and LLM audit robustness on paraphrased real-trace ledger claims
- Success threshold: On paraphrased claims, at least one LLM auditor and the human sample achieve >=0.80 accuracy and >=0.70 evidence citation F1, beat retrieval-only and majority baselines by >=0.15 accuracy, and degrade by <=0.10 accuracy from template claims.
- Stop condition: Stop as no-paper if LLM/human auditors do not beat retrieval-only and majority baselines by >=0.10 accuracy, or if paraphrase variants break label/evidence agreement below 0.95 structured-oracle accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/human-llm-natural-claim-audit-benchmark-for-real-trace-evi-94500e4a0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
