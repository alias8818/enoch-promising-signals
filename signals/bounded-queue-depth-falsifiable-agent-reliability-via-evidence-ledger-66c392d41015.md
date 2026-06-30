# Bounded Queue Depth Falsifiable Agent Reliability via Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-queue-depth-falsifiable-agent-reliability-via-evidence-ledger-66c392d41015`
Run ID: `bounded-queue-depth-falsifiable-agent-reliability-via-evidence-ledger-66c392d41015-20260605T203008599308+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d7ba9c7bd4a7

## What looked useful

Main overloaded run: bounded_ledger achieved 0.9526 claim accuracy vs 0.9487 for unbounded_ledger and 0.9400 for unbounded_no_ledger; unsupported claim rate was 0.0 with ledger vs 1.0 without; invalid-claim locator rate was 1.0 with ledger vs 0.0054 for unbounded_no_ledger; p90 latency fell from 27 to 12 ticks with queue depth 64, while drop rate rose to 0.2828. No-overload control removed the bounded-vs-unbounded ledger accuracy difference.

## Boundaries and scale limits

Evidence is simulator-only: no real LLM agent, no external tool environment, no human audit study, no production queue, and no natural-language evidence records. Main run used 5,000 episodes per policy and sensitivity runs used 1,000 episodes per setting.

## Claim scope

In a synthetic overloaded agent-auditor simulator with observable ground truth, a claim-to-evidence ledger eliminates unsupported emitted claims and makes invalid claims locatable; adding bounded queue depth reduces stale backlog and modestly improves claim accuracy under overload, at the cost of dropping obligations.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but cannot justify a paper-positive claim about real agent reliability.

## Recommended next action

Run a bounded real-agent benchmark where natural-language claims must cite tool/retrieval evidence IDs and compare bounded evidence-obligation queues against unbounded scratchpad/queue baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Queue Benchmark
- Success threshold: Ledger+bounded queue reduces unsupported claims by at least 50% and audit locator failures by at least 50% versus the strongest baseline while preserving at least 95% of baseline task success on a minimum 200-task benchmark.
- Stop condition: Stop if unsupported claims or locator failures do not improve by at least 20% after the first 50 real tasks, or if task success falls below 90% of baseline under the bounded queue.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-depth-falsifiable-agent-reliability-via-evidence-ledger-66c392d41015`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
