# LLM ReAct Ledger Audit on Paraphrased Natural Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `llm-react-ledger-audit-on-paraphrased-natural-traces-f035edca3a`
Run ID: `llm-react-ledger-audit-on-paraphrased-natural-traces-f035edca3a-20260529T162003616658+0000`

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

- Parent run decision: Real-Agent Natural-Language ReAct Ledger Audit: enoch://control-plane/projects/real-agent-natural-language-react-ledger-audit-d7f4987e53/runs/real-agent-natural-language-react-ledger-audit-d7f4987e53-20260529T092003455864+0000
- Parent run decision: Live CPU ReAct Evidence Ledger Against Schema-Only Tool Traces: enoch://control-plane/projects/live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5/runs/live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5-20260529T051343320572+0000

## What looked useful

Stable-key paraphrased traces: ledger F1 1.0000 versus format baseline 0.6656, lexical baseline 0.5200, and no-tool ablation 0.7663 across 25,000 examples. Canonical traces: ledger F1 1.0000 versus 0.1126, 0.5132, and 0.7624 respectively. Alias-changing paraphrase stress reduced ledger F1 to 0.6656, showing schema-free key paraphrase is the main boundary.

## Boundaries and scale limits

Validation used synthetic generated traces, deterministic paraphrase templates, four task domains, five seeds, 50,000 primary examples, and a 25,000-example alias stress test on a CPU worker. It did not use real LLM trajectories, human paraphrases, model-judged semantic extraction, or open-ended tool schemas.

## Claim scope

On fixed-seed generated ReAct-style traces where paraphrasing preserves stable ledger field identifiers, a ledger auditor that checks action-expression to observation consistency and final-answer to latest-observation consistency detects injected trace faults better than format, lexical, and no-tool ablation baselines.

## Why it stopped

Mechanism is supported only under stable-key synthetic paraphrase and fails under alias-changing paraphrase without schema support, so the evidence is not publication-grade.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should add schema-aware alias extraction and evaluate on real LLM or human-paraphrased ReAct traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Schema-Aware Ledger Audit on Alias-Paraphrased ReAct Traces
- Success threshold: On at least 1000 alias-paraphrased natural traces, schema-aware ledger audit improves F1 by at least 0.15 over the best non-ledger baseline with bootstrap 95% CI lower bound above 0.05 while keeping false-positive rate on clean traces below 10%.
- Stop condition: Stop if alias resolution cannot recover field alignment above 90% on clean traces or if the schema-aware ledger auditor fails to beat the best baseline by at least 0.05 F1 in a 300-example pilot.

## Evidence references

- Artifact root: `<local-path>/projects/llm-react-ledger-audit-on-paraphrased-natural-traces-f035edca3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
