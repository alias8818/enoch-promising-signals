# Evidence-Ledger Agents: Forcing Falsifiable Claims Before Actions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agents-forcing-falsifiable-claims-before-actions-8fbc17cb8d30`
Run ID: `evidence-ledger-agents-forcing-falsifiable-claims-before-actions-8fbc17cb8d30-20260612T003201893539+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f44ce5341be3

## What looked useful

Across 10 replicates of 5,000 episodes per regime, informative-probe ledger wrong-action rate averaged 0.03202 versus 0.3218 for action-first and claim-only controls, with mean act rate 0.69072 and mean 1.7462 probes. Claim-only did not improve over action-first. Under weak probes, the ledger mostly abstained, so the mechanism depends on informative independent evidence.

## Boundaries and scale limits

Local CPU-only synthetic simulation; no LLM agents, no natural-language evidence, no real tool-use tasks, no adversarial agents, and no field validation. Weak probes caused near-total abstention rather than useful task performance.

## Claim scope

In a synthetic three-state noisy decision task, an evidence ledger that forces a pre-action claim, explicit disconfirmation condition, and posterior support threshold reduces wrong acted decisions versus action-first and claim-only controls when follow-up probes are informative.

## Why it stopped

Closed as no-paper useful signal: evidence supports the synthetic mechanism but is proxy-only and insufficient for a paper or broad agent claim.

## Recommended next action

Run a bounded deepen follow-up in a real tool-using LLM harness with externally checkable outcomes, comparing action-first, claim-only, and evidence-ledger prompts on wrong actions, unsupported actions, abstention, latency, and evidence quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating in real tool-using LLM tasks
- Success threshold: Evidence-ledger condition reduces wrong or unsupported actions by at least 30% relative to both controls while retaining at least 80% of the best control's task success rate.
- Stop condition: Stop if the ledger condition fails to reduce wrong or unsupported actions by at least 15% in the first 50 tasks or if abstention exceeds 50% without corresponding safety gains.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agents-forcing-falsifiable-claims-before-actions-8fbc17cb8d30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
