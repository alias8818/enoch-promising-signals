# LLM File-Agent Evidence Ledger on Hidden-Drift Local Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-file-agent-evidence-ledger-on-hidden-drift-local-tasks-4b202643bc`
Run ID: `llm-file-agent-evidence-ledger-on-hidden-drift-local-tasks-4b202643bc-20260611T133203602410+0000`

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

- Parent run decision: Mandatory Evidence-Ledger Agent on Local Multi-Step Tasks: enoch://control-plane/projects/mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153/runs/mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153-20260611T110701531659+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59f60beba17

## What looked useful

Across 480 controlled trials, the baseline succeeded on 41.67% of trials with a 50.00% stale-overwrite rate, while the ledger variant succeeded on 100.00%, detected 100.00% of injected drifts, and had 0.00% stale overwrites.

## Boundaries and scale limits

Tested only scripted agents, one small synthetic config file, 3 task families, 4 drift modes, and 20 seeds per cell. It did not test real LLM tool calls, large repositories, concurrent process races, multi-file semantic dependencies, or long-horizon agent behavior.

## Claim scope

In a deterministic small local file-agent harness with single-file hidden drift injected between observe and edit, a hash-backed evidence ledger with pre-edit revalidation eliminated stale-file failures relative to a no-revalidation baseline.

## Why it stopped

Tier 1 controlled direct test completed; result is a useful mechanism signal but not paper-ready because LLM behavior and realistic repositories were only proxied.

## Recommended next action

Run a bounded real-LLM deepen test using the same hidden-drift harness wrapped as file tools, comparing no-ledger prompting against ledger-enforced revalidation on at least 30 tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Tool-Agent Hidden-Drift Ledger Test
- Success threshold: Ledger condition reduces stale-overwrite rate by at least 50% versus no-ledger baseline without reducing overall task success by more than 10 percentage points.
- Stop condition: Stop if the ledger wrapper cannot be made to enforce pre-write validation, or if paired LLM runs show less than a 10 percentage point stale-overwrite reduction after 30 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/llm-file-agent-evidence-ledger-on-hidden-drift-local-tasks-4b202643bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
