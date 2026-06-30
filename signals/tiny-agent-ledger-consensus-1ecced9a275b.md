# Tiny Agent Ledger Consensus

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-agent-ledger-consensus-1ecced9a275b`
Run ID: `tiny-agent-ledger-consensus-1ecced9a275b-20260530T025021323269+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/22735ade539b

## What looked useful

Ledger gossip improved mean agreement from 0.7703 to 0.9684 and mean consensus accuracy from 0.7276 to 0.8821 across 108 paired synthetic conditions; it won 91 conditions and had 3 small no-drop regressions.

## Boundaries and scale limits

No real LLM agents, no real tool traces, no cryptographic signatures, no Sybil resistance, no adversarial scheduler, and no production ledger overhead were tested. The run lasted 19 seconds and should be treated as a small synthetic mechanism probe.

## Claim scope

In a synthetic binary consensus proxy with 5-11 agents, 0-2 Byzantine equivocators, message drops up to 0.5, observation noise up to 0.35, and 4 gossip rounds, append-only ledger gossip with deterministic equivocation exclusion improved mean honest-agent agreement and consensus accuracy over ephemeral message voting.

## Why it stopped

Synthetic proxy produced useful mechanism evidence but not direct/full validation of tiny agent ledger consensus in realistic agent workflows.

## Recommended next action

Run a bounded deepen test using real multi-agent task traces with ablations for persistence, gossip rounds, and equivocation filtering; do not write a paper from this synthetic proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Tiny Agent Ledger Consensus Ablation
- Success threshold: Full ledger gossip improves agreement by at least 10 percentage points over ephemeral voting with no more than 3 percentage points task-accuracy regression and less than 2x latency/log overhead on the bounded trace suite.
- Stop condition: Stop if ledger variants fail to improve agreement by 5 percentage points on at least two task families or introduce more than 5 percentage points task-accuracy loss.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-ledger-consensus-1ecced9a275b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
