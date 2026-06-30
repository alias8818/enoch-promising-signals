# Evidence ledger for small CPU agent tool reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-cpu-agent-tool-reliability-9f060c27a2f8`
Run ID: `evidence-ledger-for-small-cpu-agent-tool-reliability-9f060c27a2f8-20260528T140214033130+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/72faf9de0682

## What looked useful

A minimal evidence ledger can block unsupported final claims in a bounded small-agent tool harness, but it does not verify the truth of supported observations and is not yet validated on real LLM agent traces.

## Boundaries and scale limits

Synthetic stochastic policies only; no live LLM, natural-language support matching, real tool latency, ambiguous answers, adversarial observations, or multi-hop production traces were tested.

## Claim scope

In a synthetic deterministic tool-use harness with noisy small-agent policies, an exact-match evidence ledger gate reduced unsupported final answers from about 17.16% to about 0.002% over 150,000 episodes per agent, while improving accuracy by about 16.80 percentage points at about 0.124 extra tool calls per episode.

## Why it stopped

Closed as a no-paper useful signal because the evidence is synthetic/proxy-only, despite clear support for the mechanism inside the local harness.

## Recommended next action

Run a bounded real-agent follow-up using the same ledger gate on at least 100 held-out tool-use tasks with a small local or API model, comparing unsupported final claims, accuracy, false rejections, and tool-call overhead against an ungated baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model evidence-ledger validation on held-out tool tasks
- Success threshold: Unsupported final-claim rate reduced by at least 50% versus baseline, relative tool-call overhead below 25%, and final accuracy not worse by more than 5 percentage points.
- Stop condition: Stop if unsupported final claims are below 2% in the baseline, if ledger false rejections exceed 10%, or if tool-call overhead exceeds 50% before meeting the unsupported-claim reduction threshold.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-cpu-agent-tool-reliability-9f060c27a2f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
