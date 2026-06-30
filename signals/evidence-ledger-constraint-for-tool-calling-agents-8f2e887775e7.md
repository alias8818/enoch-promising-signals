# Evidence-Ledger Constraint for Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-tool-calling-agents-8f2e887775e7`
Run ID: `evidence-ledger-constraint-for-tool-calling-agents-8f2e887775e7-20260531T183513739735+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4e31330fce0a

## What looked useful

Main run: unconstrained baseline emitted 6,129 unsupported/contradicted claims out of 20,000 final claims (30.645%). Ledger-constrained generation emitted 0 unsupported claims and 20,000 accepted supported claims. With 75% evidence loss it still emitted 0 unsupported claims but only 7,435 accepted supported claims, showing an abstention/yield cost.

## Boundaries and scale limits

No real LLMs, natural-language entailment, multi-hop reasoning, adversarial tools, or user-task benchmark were tested. The evidence is a local CPU Monte Carlo mechanism test over 5,000 synthetic tasks plus evidence-loss ablations.

## Claim scope

In a synthetic structured tool-trace harness with exact normalized fact matching, requiring final claims to cite entailing evidence-ledger entries eliminated unsupported and contradicted final claims, while incomplete ledgers reduced answer yield.

## Why it stopped

No-paper closure: this is useful synthetic mechanism evidence, not direct publication-grade validation on real tool-calling agents.

## Recommended next action

Run a bounded real-LLM trace benchmark with programmatic tools and labeled claim support to test whether the constraint improves factual support without unacceptable answer-yield loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM Evidence-Ledger Trace Benchmark
- Success threshold: Unsupported final-claim rate falls by >=80% versus unconstrained baseline, supported-claim yield remains >=70% of baseline supported claims, and format failures stay below 10%.
- Stop condition: Stop if the ledger validator rejects >40% of otherwise supported claims after prompt iteration or if unsupported-claim reduction is <50% on the first 100 labeled real-agent traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-tool-calling-agents-8f2e887775e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
