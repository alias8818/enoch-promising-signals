# Evidence ledger to reduce tool hallucinations in tiny agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-to-reduce-tool-hallucinations-in-tiny-agents-71a995c37bec`
Run ID: `evidence-ledger-to-reduce-tool-hallucinations-in-tiny-agents-71a995c37bec-20260608T111301178904+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5936459271af

## What looked useful

The mechanism is useful as a bounded runtime guardrail: binding final answers to recorded tool observations removes unsupported factual tool claims in the simulator, but trades off answer coverage and leaves arithmetic errors unless separately checked.

## Boundaries and scale limits

The result is synthetic and CPU-only. It does not validate real tiny LLM agents, production tool parsers, adversarial tools, multi-hop natural-language traces, or serving latency effects.

## Claim scope

In a deterministic synthetic tiny-agent tool benchmark, an evidence-ledger finalizer reduced unsupported tool claims from 23.0% in baseline and 12.3% in a self-check control to 0.0%, while increasing abstention to 34.4%.

## Why it stopped

No-paper closure because the evidence is a synthetic mechanism test rather than direct real-agent validation.

## Recommended next action

Run a bounded direct follow-up on actual small language-model agents using the same task family, comparing identical prompts and tools with and without ledger-constrained finalization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct ledger grounding test on small tool-using language-model agents
- Success threshold: Unsupported tool-claim rate falls by at least 80% versus baseline and is below 5%, with exact answer rate no worse than baseline by more than 10 percentage points.
- Stop condition: Stop if ledger finalization fails to reduce unsupported claims by at least 50% on the first 200 real-agent episodes or if parsing/tool-call failures prevent comparable traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-to-reduce-tool-hallucinations-in-tiny-agents-71a995c37bec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
