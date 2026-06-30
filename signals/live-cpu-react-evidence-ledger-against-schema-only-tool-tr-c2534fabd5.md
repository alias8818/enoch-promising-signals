# Live CPU ReAct Evidence Ledger Against Schema-Only Tool Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5`
Run ID: `live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5-20260529T051343320572+0000`

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

- Parent run decision: Falsifiable Evidence Ledger for CPU ReAct Agents: enoch://control-plane/projects/falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7/runs/falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7-20260528T231903427362+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57b4ce2850fe

## What looked useful

Schema-only tool traces were insufficient for value-level claim auditing: mean unsupported-claim recall was 0.2872 versus 1.0000 for the live ledger. Live ledger mean F1 was 1.0000, audit cost was 0.00222 ms/claim, and serialized ledger size was 21.5% of raw retained trace size. The mechanism is supported, but the result is no-paper because retaining raw outputs produced the same audit accuracy.

## Boundaries and scale limits

500 tasks across 5 seeds with deterministic lookup tools, structured claims, and synthetic evidence. The run does not test real LLM ReAct behavior, natural-language claim extraction, noisy/adversarial tools, production tracing, or human-labeled external tasks. Posthoc raw-output retention matched the live ledger exactly.

## Claim scope

In a controlled CPU-local structured ReAct trace benchmark, a live normalized evidence ledger enables exact final-answer claim support auditing and substantially improves unsupported-claim detection compared with schema-only tool traces that omit concrete observed values.

## Why it stopped

Tier 1 controlled direct test passed its mechanism threshold, but evidence is not publication-grade and does not show uniqueness over posthoc raw-output retention.

## Recommended next action

Run a bounded real-agent follow-up with natural-language ReAct traces, claim extraction, and human/auditable gold labels to test whether the ledger advantage persists beyond structured synthetic claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Natural-Language ReAct Ledger Audit
- Success threshold: Across at least 100 real-agent tasks, live ledger unsupported-claim recall exceeds schema-only by >= 0.25, live ledger F1 is >= 0.90 or within 0.05 of raw-output retention, and ledger serialized size is <= 50% of raw trace size.
- Stop condition: Stop if natural-language extraction/gold-label noise prevents reliable support labels, or if live ledger unsupported-claim recall improves by < 0.10 over schema-only on the first 50 labeled tasks.

## Evidence references

- Artifact root: `<local-path>/projects/live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
