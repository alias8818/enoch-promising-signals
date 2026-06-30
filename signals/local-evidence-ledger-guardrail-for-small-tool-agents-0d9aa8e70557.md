# Local evidence-ledger guardrail for small tool agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-evidence-ledger-guardrail-for-small-tool-agents-0d9aa8e70557`
Run ID: `local-evidence-ledger-guardrail-for-small-tool-agents-0d9aa8e70557-20260529T082551931302+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8d22261cc54

## What looked useful

Across 20,000 synthetic tasks, baseline accepted 6,107/6,107 unsupported claims, while the ledger guardrail accepted 0/6,107 unsupported claims and false-blocked 0/13,893 supported claims; median validation overhead was about 10.2 microseconds in local Python.

## Boundaries and scale limits

No real LLM agents, natural-language claim extraction, production tools, adversarial prompt suite, multi-turn planning, large outputs, or user-facing repair loop were tested. Evidence is local and synthetic, not publication-grade deployment evidence.

## Claim scope

In a deterministic synthetic benchmark with structured one-claim final answers over four toy tools, a local append-only evidence ledger plus exact citation validator blocked all unsupported claims injected by simulated small tool agents without false-blocking supported claims.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but it is not direct real-agent evidence and should not be treated as full validation.

## Recommended next action

Run a bounded real-agent follow-up with small LLM tool agents, natural-language answer claim extraction, and no-ledger/cite-only controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-agent evidence-ledger guardrail benchmark
- Success threshold: Ledger guardrail reduces unsupported-claim leakage by at least 80% relative to cite-only baseline, keeps false-block rate below 5%, and adds less than 20% median end-to-end latency on at least 300 tasks.
- Stop condition: Stop as negative if unsupported-claim leakage remains above 10% or false-block rate exceeds 10% after prompt/schema fixes on the first 100 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/local-evidence-ledger-guardrail-for-small-tool-agents-0d9aa8e70557`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
