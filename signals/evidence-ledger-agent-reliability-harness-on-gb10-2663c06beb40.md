# Evidence-Ledger Agent Reliability Harness on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40`
Run ID: `evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40-20260630T084812042004+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

The project now contains a reproducible harness showing the expected reliability tradeoff: ledger-gated policies eliminated unsupported claims in controlled missing/conflict/distractor cases, while baseline loose and retrieval-only policies emitted unsupported answers on 55.0% and 49.25% of cases respectively.

## Boundaries and scale limits

Synthetic/proxy policies only; no live LLM, production agent, real retrieval corpus, adversarial paraphrase set, or long GB10 inference run was evaluated.

## Claim scope

In a deterministic synthetic evidence-grounded QA harness with 400 generated cases, strict claim-level evidence-ledger gating reduced unsupported and contradicted outputs to zero while answering 50% of cases.

## Why it stopped

No-paper useful signal: the result is a synthetic/proxy mechanism confirmation, not direct/full validation of an agent reliability benchmark.

## Recommended next action

Run the same harness against a live local LLM/agent with blinded evidence packs and compare prompt-only citation instructions against enforced ledger verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-LLM evidence-ledger reliability harness
- Success threshold: Ledger condition has at least 50% lower unsupported rate than prompt-only citation baseline with 95% confidence interval separation and at least 35% coverage.
- Stop condition: Stop if the live model endpoint cannot produce parseable claim/citation outputs after two prompt formats, or if ledger gating fails to reduce unsupported rate by at least 25% on the first 100 cases.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
