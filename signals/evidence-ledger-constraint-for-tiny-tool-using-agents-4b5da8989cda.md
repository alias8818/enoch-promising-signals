# Evidence-Ledger Constraint for Tiny Tool-Using Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda`
Run ID: `evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda-20260524T084003946062+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57c7e86ee078

## What looked useful

Evidence-ledger answer gating appears useful as a runtime constraint when agents have noisy priors and callable tools. Retry is essential: no-retry ledger gating caused about 50.5% abstention, while two-call retry kept abstention below 1% in the main proxy. The core limitation is false tool evidence; at 10% tool corruption, unsupported finals rose to 9.3%.

## Boundaries and scale limits

Proxy-only evidence: no real LLM weights, real tool APIs, open-ended traces, human support labels, prompt injection tests, or production latency/observability measurements were evaluated.

## Claim scope

In a deterministic synthetic benchmark of tiny stochastic tool-using policies, requiring final answers to be supported by a structured evidence ledger reduced unsupported final answers from 0.5067 to 0.0291 with a two-call retry budget, while increasing accuracy from 0.7308 to 0.9652.

## Why it stopped

Closed as no-paper useful signal because the mechanism was supported only in synthetic stochastic-policy proxies, not in direct real tiny LLM agent evidence.

## Recommended next action

Run a bounded real-agent follow-up with 0.5B-3B instruction/tool models on held-out tool QA tasks, comparing unconstrained, ledger-no-retry, and ledger-retry under matched tool-call budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-LLM Evidence-Ledger Tool-Use Evaluation
- Success threshold: Ledger-retry reduces unsupported final answers by >=50% relative to unconstrained baseline, keeps exact-match accuracy within 5 absolute points of or above baseline, and adds no more than 2x mean tool calls.
- Stop condition: Stop if ledger-retry fails the unsupported-answer reduction threshold on both tested models, or if abstention exceeds 20% at matched tool-call budget.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
